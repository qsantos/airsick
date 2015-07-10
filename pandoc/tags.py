#!/usr/bin/env python
"""Custom HTML tags

Add custom tags <remark> and <important>.
Export <remark>, <important>, <figure> and <figcaption> to LaTeX.
"""

import pandocfilters


figure_depth = 0


def filter(key, value, format, meta):
    # look for raw HTML code
    if key not in ('RawInline', 'RawBlock'):
        return None
    lang, code = value
    if lang != 'html':
        return None

    # picks mapping depending on export format
    if format in ('html', 'html5'):
        lang = 'html'
        mapping = {
            '<remark>': '<div class="remark">',
            '</remark>': '</div>',
            '<important>': '<div class="important">',
            '</important>': '</div>',
        }
    elif format == 'latex':
        lang = 'tex'

        # dirty hack for LaTeX subfigures
        global figure_depth
        if code == '<figure>':
            figure_depth += 1
            if figure_depth > 1:
                code = r'\begin{subfigure}{0.45\textwidth}'
                return pandocfilters.RawBlock(lang, code)
        elif code == '</figure>':
            figure_depth -= 1
            if figure_depth > 0:
                code = r'\end{subfigure}\gobblepars'
                return pandocfilters.RawBlock(lang, code)

        mapping = {
            '<remark>': r'\begin{remark}\gobblepars',
            '</remark>': r'\end{remark}',
            '<important>': r'\begin{important}\gobblepars',
            '</important>': r'\end{important}',
            '<figure>': r'\begin{figure}[H]\centering',
            '</figure>': r'\end{figure}',
            '<figcaption>': r'\caption[]{\gobblepars',
            '</figcaption>': '}',
        }
    else:
        return None

    # do the mapping
    code = mapping.get(code, code)

    if key == 'RawInline':
        return pandocfilters.RawInline(lang, code)
    else:
        return pandocfilters.RawBlock(lang, code)


if __name__ == "__main__":
    pandocfilters.toJSONFilter(filter)
