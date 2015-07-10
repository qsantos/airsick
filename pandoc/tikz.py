#!/usr/bin/env python
"""Build TikZ figures as SVGs"""

import pandocfilters
import subprocess
import hashlib
import os
import sys

basedir = "web"
imagedir = "figures"


def tex2image(tex, outfile):
    """Convert LaTeX to SVG"""

    tex = (
        r'\documentclass{standalone}'  # crop the viewport
        r'\input{header}'  # usual LaTeX stuff
        r'\input{drawing}'  # needed for drawing
        r'\begin{document}'
        '\n%s\n'
        r'\end{document}'
        '\n'
        % tex
    )

    # make .tex file
    filename = os.path.join(tempdir, 'tikz.tex')
    with open(filename, 'w') as f:
        f.write(tex)

    # make .dvi from .tex
    p = subprocess.call(["latex", "-output-directory", tempdir, filename],
                        stdout=sys.stderr)

    # compilation failed
    if p != 0:
        sys.stderr.write(tex)
        shutil.rmtree(tempdir)
        sys.exit(p)

    # make .svg from .dvi
    filename = os.path.join(tempdir, 'tikz.dvi')
    p = subprocess.call(['dvisvgm', '--no-fonts', filename, '-o', outfile])

    # conversion failed
    if p != 0:
        shutil.rmtree(tempdir)
        sys.exit(p)


def filter(key, value, format, meta):
    # look for a raw TikZ block
    if key != 'RawBlock':
        return None
    lang, code = value
    if lang != 'latex':
        return None
    if not code.startswith(r"\begin{tikzpicture}"):
        return None

    # pick a deterministic file name
    hash = hashlib.sha1(code.encode()).hexdigest()
    filename = os.path.join(imagedir, hash + '.svg')
    outfile = os.path.join(basedir, filename)

    # create the figure, if not already done
    if not os.path.isfile(outfile):
        try:
            os.mkdir(os.path.join(basedir, imagedir))
        except OSError:
            pass
        tex2image(code, outfile)

    image = pandocfilters.Image([], [filename, "TikZ figure"])
    return pandocfilters.Para([image])


if __name__ == "__main__":
    import tempfile
    import shutil

    # directory for temporary files
    tempdir = tempfile.mkdtemp()

    pandocfilters.toJSONFilter(filter)

    # clean up
    shutil.rmtree(tempdir)
