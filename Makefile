TARGET   = airsick.pdf
BUILDDIR = .build

all: $(TARGET)

# http://tex.stackexchange.com/questions/13271/13277#13277
%.pdf: %.tex $(wildcard *.tex) $(wildcard data/*)
	@mkdir -p "$(BUILDDIR)/$(BUILDDIR)/"
	@openout_any=a pdflatex -halt-on-error -shell-escape -output-dir "$(BUILDDIR)" $*
	@mv "$(BUILDDIR)/$@" .

optimize: all
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=airsick_opt.pdf airsick.pdf

toc: all
	pdflatex -halt-on-error -shell-escape "$(TARGET:.pdf=.tex)"

clean:
	rm -Rf "$(BUILDDIR)/"

destroy: clean
	rm -f "$(TARGET)"

rebuild: destroy all
