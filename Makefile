all: airsick.pdf

%.pdf: %.tex $(wildcard *.tex) $(wildcard data/)
	pdflatex -halt-on-error $*

toc: all
	pdflatex -halt-on-error airsick

clean:
	rm -f *.aux *.log *.out *.toc
