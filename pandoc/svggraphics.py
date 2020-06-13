#!/usr/bin/env python3
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

    properties, alternate_text, (filename, title) = value
    if not filename.endswith('.svg'):
        return None

    # make .dvi from .tex
    basename = filename[4:-4]  # strips ^img/ and .svg$
    pdffile = os.path.join(builddir, basename + '.pdf')
    subprocess.check_call(["inkscape", filename, '--export-pdf', pdffile])

    return pandocfilters.Image(properties, alternate_text, (pdffile, title))


if __name__ == "__main__":
    # ensure build directory exists
    try:
        os.mkdir(builddir)
    except OSError:
        pass

    pandocfilters.toJSONFilter(filter)
