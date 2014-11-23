TARGETS = airsick.pdf

all: $(TARGETS)

%.pdf: %.tex $(wildcard *.tex) $(wildcard data/*)
	pdflatex -halt-on-error $*

toc: all
	pdflatex -halt-on-error airsick

clean:
	rm -f *.aux *.log *.out *.toc

destroy: clean
	rm -f $(TARGETS)

rebuild: destroy all
