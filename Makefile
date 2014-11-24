TARGETS = airsick.pdf

all: $(TARGETS)

%.pdf: %.tex $(wildcard *.tex) $(wildcard data/*) figures/
	pdflatex -halt-on-error -shell-escape $*

%/:
	mkdir -p $@

toc: all
	pdflatex -halt-on-error -shell-escape airsick

clean:
	rm -f *.aux *.log *.out *.toc *.auxlock figures/*

destroy: clean
	rm -f $(TARGETS)

rebuild: destroy all
