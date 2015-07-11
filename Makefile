TARGET   = airsick.pdf
BUILDDIR = .build
WEBDIR   = web
SRC = $(wildcard *.md)
HTML = $(addprefix $(WEBDIR)/, $(patsubst %.md,%.html,$(SRC)))
TEX  = $(patsubst %.md,%.tex,$(SRC))

all: pdf web

pdf: $(TARGET) $(TEX)

web: $(addprefix $(WEBDIR)/, $(patsubst %.md,%.html,$(SRC)))

# http://tex.stackexchange.com/questions/13271/13277#13277
%.pdf: %.tex $(wildcard *.tex) $(TEX) $(wildcard data/*)
	@echo $@
	@mkdir -p "$(BUILDDIR)/$(BUILDDIR)/"
	@pdflatex -halt-on-error -output-dir "$(BUILDDIR)" $*
	@mv "$(BUILDDIR)/$@" .

%.tex: %.md
	@echo $@
	@pandoc $< --biblatex --template pandoc/template.tex -o $@ \
		--filter=pandoc/quote.py \
		--filter=pandoc/tags.py \
		--filter=pandoc/tikz.py \

$(WEBDIR)/%.html: %.md
	@echo $@
	@mkdir -p "$(WEBDIR)/figures/"
	@pandoc $< -t html5 -s --css=style.css -H pandoc/header.html --toc --toc-depth=1 -o $@ \
		--filter=pandoc/quote.py \
		--filter=pandoc/citations.py \
		--filter=pandoc/tags.py \
		--filter=pandoc/mathml.py \
		--filter=pandoc/tikz.py \

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
