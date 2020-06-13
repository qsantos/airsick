#!/usr/bin/env python3
"""Handle citations"""
import json
import subprocess
from typing import Any, Dict, Iterator, TextIO, Tuple

import pandocfilters


def parse_bib_item(code: str, from_: str = 'markdown') -> Any:
    """Parse code using Pandoc"""
    pandoc_process = subprocess.Popen(
        ['pandoc', '-f', from_, '-t', 'json'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    )
    stdout, _ = pandoc_process.communicate(code.encode())
    return json.loads(stdout)['blocks']


def iter_bib_items(f: TextIO) -> Iterator[Tuple[str, str]]:
    """List items of a LaTeX bibliograph"""
    for line in f:
        if line.startswith(r'\bibitem{') and line.endswith('}\n'):
            # extract key, value
            yield line[9:-2], '\n'.join(iter(lambda: next(f).strip(), ''))


def parse_bib(f: TextIO) -> Dict:
    """Parse a LaTeX bibliography to Pandoc intermediate representation"""
    return {
        key: [pandocfilters.Div([key, [], []], parse_bib_item(value, 'latex'))]
        for key, value in iter_bib_items(f)
    }


citations = []


def filter(key: str, value: str, format: str, meta: Dict) -> Any:
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
    link = '#' + citation
    title = citation
    return [
        pandocfilters.Str('['),
        pandocfilters.Link(['', [], []], [text], [link, title]),
        pandocfilters.Str(']'),
    ]


if __name__ == '__main__':
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
