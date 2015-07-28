#!/usr/bin/env python
"""Convert SVG images to PDF for LaTeX"""

import pandocfilters
import subprocess
import os

builddir = '.build'


def filter(key, value, format, meta):
    if format != 'latex':
        return None

    if key != 'Image':
        return None

    _, (filename, alternate_text) = value
    if not filename.endswith('.svg'):
        return None

    # make .dvi from .tex
    basename = filename[4:-4]  # strips ^img/ and .svg$
    pdffile = os.path.join(builddir, basename + '.pdf')
    subprocess.check_call(["inkscape", filename, '--export-pdf', pdffile])

    return pandocfilters.Image(_, (pdffile, alternate_text))


if __name__ == "__main__":
    # ensure build directory exists
    try:
        os.mkdir(builddir)
    except OSError:
        pass

    pandocfilters.toJSONFilter(filter)
