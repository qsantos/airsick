#!/usr/bin/env python3
"""Sourced quotes"""

import pandocfilters


def rindex(self, value):
    """Return last index of value"""
    reversed_index = self[::-1].index(value)
    return len(self)-1 - reversed_index


def filter(key, value, format, meta):
    if key != 'BlockQuote':
        return None

    # extract source from quote
    last_paragraph = value[-1]['c']
    try:
        idx = rindex(last_paragraph, {'c': '--', 't': 'Str'})
    except ValueError:
        return None
    cite = last_paragraph[idx+2:]  # strip '--' and first space
    last_paragraph[idx-1:] = []  # strip last space

    # export
    if format in ('html', 'html5'):
        return [
            pandocfilters.BlockQuote(value),
            pandocfilters.Plain(
                [pandocfilters.RawInline('html', '<cite>')] +
                cite +
                [pandocfilters.RawInline('html', '</cite>')]
            )
        ]
    elif format == 'latex':
        return pandocfilters.Plain(
            [pandocfilters.RawInline('latex', r'\chaptquote{')] +
            cite +
            [pandocfilters.RawInline('latex', '}{')] +
            value[0]['c'] +  # assume there is only one paragraph
            [pandocfilters.RawInline('latex', '}')]
        )

    return None

if __name__ == "__main__":
    pandocfilters.toJSONFilter(filter)
