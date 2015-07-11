TARGET   = airsick.pdf
BUILDDIR = .build
WEBDIR   = web
SRC = $(wildcard *.md)
HTML = $(addprefix $(WEBDIR)/,   $(patsubst %.md,%.html,$(SRC)))
TEX  = $(addprefix $(BUILDDIR)/, $(patsubst %.md,%.tex, $(SRC)))

all: pdf web

pdf: $(TARGET) $(TEX)

web: $(addprefix $(WEBDIR)/, $(patsubst %.md,%.html,$(SRC)))

# http://tex.stackexchange.com/questions/13271/13277#13277
%.pdf: %.tex $(wildcard *.tex) $(TEX) $(wildcard data/*)
	@echo $@
	@mkdir -p "$(BUILDDIR)/$(BUILDDIR)/"
	@pdflatex -halt-on-error -include-directory="$(BUILDDIR)" -output-dir="$(BUILDDIR)" $*
	@mv "$(BUILDDIR)/$@" .

$(BUILDDIR)/%.tex: %.md
	@echo $@
	@pandoc $< -t json | \
		pandoc/quote.py latex | \
		pandoc/tags.py latex | \
		pandoc/tikz.py latex | \
		pandoc -f json -t latex --biblatex --template pandoc/template.tex -o $@

$(WEBDIR)/%.html: %.md
	@echo $@
	@mkdir -p "$(WEBDIR)/figures/"
	@pandoc $< -t json | \
		pandoc/quote.py html5 | \
		pandoc/citations.py html5 | \
		pandoc/tags.py html5 | \
		pandoc/mathml.py html5 | \
		pandoc/tikz.py html5 | \
		pandoc -f json -t html5 -s --css=style.css -H pandoc/header.html --toc --toc-depth=1 -o $@

optimize: all
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=airsick_opt.pdf airsick.pdf

toc: all
	rm -f $(TARGET)
	$(MAKE)

clean:
	rm -Rf "$(BUILDDIR)/"
	rm -f $(TEX)

destroy: clean
	rm -f "$(TARGET)"
	rm -f $(WEBDIR)/*.html
	rm -Rf "$(WEBDIR)/figures/"

rebuild: destroy all
