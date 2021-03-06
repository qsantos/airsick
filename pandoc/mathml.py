#!/usr/bin/env python3
"""Export LaTeX to MathML"""
import fcntl
import os
import re
import time
from subprocess import PIPE, Popen
from typing import Any, Dict, List, Tuple

import pandocfilters


def communicate(process: Popen, command: str) -> str:
    """Send command to process, return result"""
    assert process.stdin is not None
    assert process.stdout is not None
    process.stdin.write(command.encode() + b'\x04\n')
    process.stdin.flush()
    out = ''

    for _ in range(1024):
        # give some time to ttm
        time.sleep(0.0009765625)

        # get output
        data = process.stdout.read() or b''
        out += data.decode()

        if out[-1:] == '\x04':
            return out[:-1].strip()

    raise Exception(f'ttm took too long (command <{command}>)')


# global variable
# save known references
references: List[str] = []


def find_in_sources(text: str) -> str:
    """Locate text in Markdown sources"""
    for filename in os.listdir('.'):
        if not filename.endswith('.md'):
            continue
        with open(filename) as f:
            if f.read().find(text) >= 0:
                return filename[:-3] + '.html'
    raise IndexError


def tex2span(tex: str) -> str:
    """Convert non-math LaTeX to HTML"""

    if tex.startswith(r'\ref{') and tex.endswith('}'):
        identifier = tex[5:-1]
        # look for internal reference
        try:
            reference = references.index(identifier)
        except ValueError:
            # look for external reference
            try:
                filename = find_in_sources(r'\eqtag{' + identifier + '}')
            except IndexError:
                return r'?'  # unknwon reference
            else:
                # link to external reference
                tex = r'\href{%s#%s}{*}' % (filename, identifier)
                filename = filename[:-3] + '.html'
        else:
            # link to internal reference
            tex = r'\hyperlink{%s}{%i}' % (identifier, reference + 1)

    return communicate(ttm_process, tex)


def tex2mathml(tex: str, display_style: str = 'inline') -> str:
    """Convert LaTeX to MathML"""

    # support for aligned environment
    tex = tex.replace(r'\begin{aligned}', r'\begin{array}{rl}')
    tex = tex.replace(r'\end{aligned}', r'\end{array}')

    def tagger(match: re.Match) -> str:
        identifier = match.group(1)
        reference = len(references)
        references.append(identifier)
        return r'\hypertarget{%s}{(%i)}' % (identifier, reference + 1)

    tex = re.sub(r'\\eqtag{(.*?)}', tagger, tex)

    # convert to MathML
    xml = communicate(ttm_process, tex)

    # fix <span>s in MathML
    xml = xml.replace('<span', '<mstyle')
    xml = xml.replace('</span', '</mstyle')

    # more properly sized dot
    xml = xml.replace('&middot;', '&#x2219;')

    # fix non-existent HTML entities
    xml = xml.replace('&iint;', '∬')
    xml = xml.replace('&iiint;', '∭')
    xml = xml.replace('&oint;', '∮')
    xml = xml.replace('&oiint;', '∯')
    xml = xml.replace('&oiiint;', '∰')

    # manually set display style
    # ttm does not handle it properly
    xml = '<math display="%s"' % display_style + xml[5:]  # replace '<math'

    return xml


def filter(key: str, value: Tuple[str, str], format: str, meta: Dict) -> Any:
    if key == 'RawBlock':
        # support for align* and alignat* environments
        lang, code = value
        if lang != 'latex':
            return None
        if code.startswith(r'\begin{align*}') and code.endswith(r'\end{align*}'):
            code = code[14:-12]  # remove environment
        elif code.startswith(r'\begin{alignat*}{') and code.endswith(r'\end{alignat*}'):
            start = code.index('}', 17) + 1  # skip alignat argument
            code = code[start:-14]  # remove environment
        else:
            return None
        code = r'$\begin{array}{rl}' + code + r'\end{array}$'  # known by tttm
        return pandocfilters.RawBlock('html', tex2mathml(code, 'block'))

    if key == 'RawInline':
        # support for non-math LaTeX
        lang, code = value
        if lang != 'tex':
            return None
        return pandocfilters.RawInline('html', tex2span(code))

    if key == 'Math':
        # support for usual LaTex
        info, code = value
        display_style = 'inline' if info['t'] == 'InlineMath' else 'block'
        code = tex2mathml('$' + code + '$', display_style)
        return pandocfilters.RawInline('html', code)


def define(command: str, before: str, after: str, option: bool = False) -> str:
    """Define a LaTex macro in HTML"""
    if option:
        return (
            r'\renewcommand{\%s}[2][]{'
            r'\begin{rawhtml}%s\end{rawhtml}'
            r'#2'
            r'\begin{rawhtml}%s\end{rawhtml}'
            r'}'
            % (command, before, after)
        )
    else:
        return (
            r'\renewcommand{\%s}[1]{'
            r'\begin{rawhtml}%s\end{rawhtml}'
            r'#1'
            r'\begin{rawhtml}%s\end{rawhtml}'
            r'}'
            % (command, before, after)
        )


if __name__ == '__main__':
    # START SET UP TTM

    # I really do not want block buffering, thus stdbuf
    ttm_process = Popen(
        ['stdbuf', '-o', '0', 'ttm', '-u', '-r'],
        stdin=PIPE, stdout=PIPE,
    )

    # set its stdout to non-blocking
    assert ttm_process.stdout is not None
    fd = ttm_process.stdout.fileno()
    fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)

    # send LaTeX header to ttm
    assert ttm_process.stdin is not None
    ttm_process.stdin.write((
        r'\documentclass{article}'
        + r'\input{header}'
        + define('mathbb', '<mstyle mathvariant="double-struck">', '</mstyle>')
        + define('mathcal', '<mstyle mathvariant="script">', '</mstyle>')
        + define('strike', '<menclose notation="updiagonalstrike">', '</menclose>', True)
        + r'\begin{document}'
    ).encode())

    # END SET UP TTM

    pandocfilters.toJSONFilter(filter)
