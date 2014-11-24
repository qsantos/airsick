TARGETS = airsick.pdf

all: $(TARGETS)

%.pdf: %.tex $(wildcard *.tex) $(wildcard data/*) figures/
	pdflatex -halt-on-error -shell-escape $*

%/:
	mkdir -p $@

optimize: all
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=airsick_opt.pdf airsick.pdf

toc: all
	pdflatex -halt-on-error -shell-escape airsick

clean:
	rm -f *.aux *.log *.out *.toc *.auxlock figures/*

destroy: clean
	rm -f $(TARGETS)

rebuild: destroy all
