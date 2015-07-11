#!/usr/bin/env python
"""Build TikZ figures as SVGs"""

import pandocfilters
import subprocess
import hashlib
import os
import sys
import shutil

builddir = '.build'


def tex2image(tex, extension='svg'):
    """Convert LaTeX to SVG or PDF"""

    # pick a deterministic file name
    hash = hashlib.sha1(tex.encode()).hexdigest()
    basename = os.path.join(builddir, hash)

    # make .tex file
    texfile = basename + '.tex'
    if not os.path.isfile(texfile):
        with open(texfile, 'w') as f:
            f.write(
                r'\documentclass{standalone}'  # crop the viewport
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
        subprocess.check_call(
            ["latex", "-output-directory", builddir, basename],
            stdout=sys.stderr
        )

    # make .pdf from .dvi
    if extension == 'pdf':
        pdffile = basename + '.pdf'
        if not os.path.isfile(pdffile):
            subprocess.check_call(['dvipdf', dvifile, pdffile])
        return pdffile

    # make .svg from .dvi
    if extension == 'svg':
        svgfile = basename + '.svg'
        if not os.path.isfile(svgfile):
            subprocess.check_call(['dvisvgm', '--no-fonts', dvifile, '-o', svgfile])
        return svgfile


def filter(key, value, format, meta):
    # look for a raw TikZ block
    if key != 'RawBlock':
        return None
    lang, code = value
    if lang != 'latex':
        return None
    if not code.startswith(r"\begin{tikzpicture}"):
        return None

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

    image = pandocfilters.Image([], [filename, "TikZ figure"])
    return pandocfilters.Para([image])


if __name__ == "__main__":
    # ensure build directory exists
    try:
        os.mkdir(builddir)
    except OSError:
        pass

    pandocfilters.toJSONFilter(filter)
