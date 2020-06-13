---
title: Introduction
date: 2015-07-11
skipnumber: yes
---

> That's one small step for a man, one giant leap for mankind.
-- [Neil Armstrong](https://en.wikipedia.org/wiki/Neil_Armstrong),
first human being on the Moon

Are you curious about the “How?” behind space exploration and satellite
operating? This document might help you quench that thirst for knowledge.
Although it is still very much in the making, it tries to clearly explain the
technical terms and to guide you through the mathematics.

If some part of it seems to be unclear or lacking explanation, do not hesitate
to contact the author at [author@airsick.guide](mailto:author@airsick.guide).

Kerbal Space Program
====================

Kerbal Space Program @ksp is a rocket simulation game; it lets you build,
launch and pilot a rocket to put up
[satellites](https://en.wikipedia.org/wiki/Satellite), send
[probes](https://en.wikipedia.org/wiki/Space_probe), land
[rovers](https://en.wikipedia.org/wiki/Rover_%28space_exploration%29), and have
Kerbals do SCIENCE.

![
Mouseover text reads ”To be fair, my job at NASA was working
on robots and didn't actually involve any orbital mechanics. The
small positive slope over that period is because it turns out
that if you hang around at NASA, you get in a lot of conversations
about space.” @xkcd1356
](img/xkcd1356.png)

A big advantage a KSP player has over actual rocket crafters is that she can
have rockets exploding without having to worry about consequences.  Half the
fun of the game comes from finding out why your next rocket will fail; thus, I
urge you roll rockets to the launchpad early and not bother thinking of every
little thing that could go wrong.

Airsick will not cover the initiation to the game, since the interface is
specific to the game and prone to change. The game offers an intuitive way to
assemble rockets and has a handy interface to control the flight. Rather, it
will expose, explain and detail real principles of physics that the game
mimics. This information can be read simply for curiosity, or can serve to
design more precise launches in the game. When possible, example values will be
taken from reality or KSP.

<note>
KSP is a proprietary software. You can play the demo for free, but will be
limited to an older version with only a few parts available for building. The
demo is way harder and the complete game way richer.
</note>

<important>
This document is intended to provide information both for beginners and actual
physicists. The first few chapters are an introduction to the elementary
concepts used within this book. In every chapters accurate derivations and
complete proofs are developed wherever needed. If you are not interested in
the specifics of a demonstration or have already some knowledge of basics
physics, feel free to skip irrelevant parts.
</important>


About this document
===================

This document was written using
[Markdown](https://en.wikipedia.org/wiki/Markdown) and
[LaTeX](https://en.wikipedia.org/wiki/LaTeX). Markdown is a very simple format
for rich text; LaTeX is currently the most flexible way to write formulas and
draw complex graphs (using TiKZ).

The source is made so as to be compiled into either a PDF or a set of webpages.

* PDF: the Markdown/LaTeX source is converted to pure LaTeX using
  [Pandoc](http://pandoc.org/); the LaTeX files are then compiled with
  `pdflatex`
* HTML: the Markdown is converted to HTML using Pandoc, inline LaTeX (formulas)
  * are converted to [MathML](https://en.wikipedia.org/wiki/MathML) using
  `ttm`, and TikZ pictures are converted to SVG files using `latex` and
  `dvisgm`

A few more details:

* since several browsers still [do not support
  MathML](http://caniuse.com/#search=mathml), including Google Chrome, Opera
  and Microsoft Internet Explorer, the Javascript library
  [MathJax](https://en.wikipedia.org/wiki/MathJax) is conditionnaly enabled to
  fill the gap
* some discrepancies between PDF and HTML generations are handled by [Pandoc
  filters](http://pandoc.org/scripting.html).
* to be more precise, during the PDF generation, TikZ pictures are
  converted to individual PDFs using (`latex` and `dvipdf`)


Credits
=======

This document makes extensive use of pictures, diagrams and various
illustrations. When an external image was included as a figure, a reference to
the source is linked in the caption (e.g. @xkcd1356).

Sources for the other illustrations:

* front cover @threekerbalmun
* chapter banners @banners
* back cover @ksp
