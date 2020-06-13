#!/usr/bin/env python3
"""Handle citations"""

import pandocfilters
import subprocess
import json


def parse(code, from_='markdown'):
    """Parse code using Pandoc"""
    pandoc_process = subprocess.Popen(
        ['pandoc', '-f', from_, '-t', 'json'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    stdout, _ = pandoc_process.communicate(code.encode())
    return json.loads(stdout)['blocks']


def bib_items(f):
    """List items of a LaTeX bibliograph"""
    for line in f:
        if line.startswith(r'\bibitem{') and line.endswith('}\n'):
            # extract key, value
            yield line[9:-2], '\n'.join(iter(lambda: next(f).strip(), ''))


def parse_bib(f):
    """Parse a LaTeX bibliography to Pandoc intermediate representation"""
    def format(arg):
        key, value = arg
        # parse and add HTML id
        return key, [pandocfilters.Div([key, [], []], parse(value, 'latex'))]
    return dict(map(format, bib_items(f)))


citations = []


def filter(key, value, format, meta):
    # look for a citation
    if key != 'Cite':
        return None
    citation = value[0][0]['citationId']

    # mark citation as used
    if citation not in citations:
        citations.append(citation)

    # display it nicely
    index = citations.index(citation) + 1
    text = pandocfilters.Str(str(index))
    link = '#'+citation
    title = citation
    return [
        pandocfilters.Str('['),
        pandocfilters.Link(['', [], []], [text], [link, title]),
        pandocfilters.Str(']'),
    ]


if __name__ == "__main__":
    import sys

    doc = json.load(sys.stdin)
    doc = pandocfilters.walk(doc, filter, 'html', doc['meta'])

    # parse bibliography
    with open('bib.tex') as f:
        bibliography = parse_bib(f)

    # append bibliography
    if citations:
        list_meta = [1, {'t': 'Decimal', 'c': []}, {'t': 'Period', 'c': []}]
        list_items = list(map(bibliography.__getitem__, citations))
        doc['blocks'] += [
            pandocfilters.HorizontalRule(),
            pandocfilters.Div(
                ['citations', [], []],
                [pandocfilters.OrderedList(list_meta, list_items)],
            )
        ]

    json.dump(doc, sys.stdout)
