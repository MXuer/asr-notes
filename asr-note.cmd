
del asr-note.pdf
xelatex -no-pdf --interaction=nonstopmode asr-note
bibtex asr-note
xelatex -no-pdf --interaction=nonstopmode asr-note
xelatex --interaction=nonstopmode asr-note

@echo off
del /q *.aux chapters\*.aux *.bbl *.blg  *.out *.toc *.bcf *.xml *.synctex *.nlo *.nls *.bak *.ind *.idx *.ilg *.lof *.lot *.ent-x *.tmp *.ltx *.los *.lol *.loc *.listing *.gz *.userbak *.nav *.snm *.vrb *.synctex(busy)


del /q *.nav *.snm *.vrb *.fls *.xdv *.fdb_latexmk 

start "" "asr-note.pdf"

