# See also /k/l/stdpreshdr.tex
NAME = dsp2seq
OTHER_DEPENDS = localremote.tex courses-overview.tex fig/*.fig eps/*.eps ../latex/*.tex ../inputs/*.sty
#OTHER_GOODIES = 
OTHER_PRODUCTS = $(NAME)_2up.pdf earth1.ps
OTHER_CLEANS = $(NAME).bm $(NAME).vrb $(NAME).aux $(NAME).toc $(NAME).idx $(NAME).ilg $(NAME).ind $(NAME).bbl .LATEX-*-TIMESTAMP .BIBTEX-TIMESTAMP $(NAME).nav $(NAME).snm $(NAME).eps
# /w/latex/Makefile.lecture
include ../latex/Makefile.lecture

KEY = DSPM
keyeps eps/$(KEY).eps: key/$(KEY).key Makefile
	-echo 'DO THIS IN KeyNote.app: key2pdf key/$(KEY).png > pdf/$(KEY).pdf'
	-echo 'pdf2ps pdf/$(KEY).pdf > eps/$(KEY).eps'
	-echo '/bin/rm pdf/$(KEY).pdf'
	-echo 'OR:'
	pdf2ps key/$(KEY).pdf > eps/$(KEY).eps

clean::
	-/bin/rm -f $(NAME).l2h
	-/bin/rm -f $(NAME).ps

# ho means "HTML open" already:
remote rem handout hout: $(NAME).pdf
	/bin/cp -p $(NAME).pdf $(NAME)-ho.pdf

local presentation pres: $(NAME).pdf
	/bin/cp -p $(NAME).pdf $(NAME)-presentation.pdf
