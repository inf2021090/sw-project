# Makefile for compiling LaTeX document and managing the docs directory

LATEX = pdflatex
BIBTEX = bibtex
REPORT = inf2021090_project_report.tex
BIBFILE = references.bib
OUTPUT = inf2021090_project_report.pdf

.PHONY: all clean clear_docs

all: $(OUTPUT)

$(OUTPUT): $(REPORT) $(BIBFILE)
	$(LATEX) $(REPORT)
	$(BIBTEX) $(basename $(REPORT))
	$(LATEX) $(REPORT)
	$(LATEX) $(REPORT)

clean:
	rm -f *.aux *.log *.bbl *.blg *.out *.toc

clear_docs:
	find docs -type f ! -name $(REPORT) ! -name $(BIBFILE) -delete


# Create environment
env:
	python -m venv

# Delete environment
delete:
	rm -rf venv

# Activate environment
activate:
	source /venv/bin/activate

# Run the Streamlit app
run:
	 streamlit run src/app.py


