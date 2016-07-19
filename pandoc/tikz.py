#!/usr/bin/env python
"""Build TikZ figures as SVGs"""

import pandocfilters
import subprocess
import hashlib
import os
import sys
import shutil

builddir = '.build'


try:  # Python 3
    devnull = subprocess.DEVNULL
except AttributeError:  # Python 2
    devnull = open(os.devnull, 'w')


def tex2image(tex, extension='svg'):
    """Convert LaTeX to SVG or PDF"""

    # pick a deterministic file name
    hash = hashlib.sha1(tex.encode()).hexdigest()
    basename = os.path.join(builddir, hash)

    # make .tex file
    texfile = basename + '.tex'
    if not os.path.isfile(texfile):
        sys.stderr.write('-> %s\n' % texfile)
        with open(texfile, 'w') as f:
            f.write(
                r'\documentclass[preview]{standalone}'  # crop the viewport
                r'\input{header}'  # usual LaTeX stuff
                r'\input{drawing}'  # needed for drawing
                r'\begin{document}'
                '\n%s\n'
                r'\end{document}' '\n'
                % tex
            )

    # make .dvi from .tex
    dvifile = basename + '.dvi'
    if not os.path.isfile(dvifile):
        sys.stderr.write('-> %s\n' % dvifile)
        subprocess.check_call(
            ["latex", "-output-directory", builddir, basename],
            stdout=devnull,
        )

    # make .pdf from .dvi
    if extension == 'pdf':
        pdffile = basename + '.pdf'
        if not os.path.isfile(pdffile):
            sys.stderr.write('-> %s\n' % pdffile)
            subprocess.check_call(
                ['dvipdf', '-dAutoRotatePages=/None', dvifile, pdffile],
                stderr=devnull,
            )
        return pdffile

    # make .svg from .dvi
    if extension == 'svg':
        svgfile = basename + '.svg'
        if not os.path.isfile(svgfile):
            sys.stderr.write('-> %s\n' % svgfile)
            subprocess.check_call(
                ['dvisvgm', '--no-fonts', dvifile, '-o', svgfile],
                stderr=devnull,
            )
        return svgfile


def filter(key, value, format, meta):
    # look for a raw TikZ block
    if key == 'Math':
        mode, code = value
    elif key == 'RawBlock':
        lang, code = value
        if lang != 'latex':
            return None
    else:
        return None

    if not code.strip().startswith(r"\begin{tikzpicture}"):
        return None

    code = code.replace(r'\^', '^')

    # create the figure, if not already done
    if format in ('html', 'html5'):
        original = tex2image(code, 'svg')
        filename = os.path.join('figures', os.path.basename(original))
        shutil.copyfile(original, os.path.join('web', filename))
    elif format == 'latex':
        filename = tex2image(code, 'pdf')
    else:
        sys.stderr.write('Unexpected format "%s"\n' % format)
        sys.exit(1)

    alternate_text = pandocfilters.Str("")
    image = pandocfilters.Image(['', [], []], [alternate_text], [filename, ""])
    if key == 'Math':
        return image
    else:  # RawBlock
        return pandocfilters.Para([image])


if __name__ == "__main__":
    # ensure build directory exists
    try:
        os.mkdir(builddir)
    except OSError:
        pass

    pandocfilters.toJSONFilter(filter)
