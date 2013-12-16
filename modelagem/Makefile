pdf:
	latexmk -pdf modelagem01
	latexmk -c
	ls -la
preview:
	subl modelagem01.tex &
	evince modelagem01.pdf &
	latexmk -pdf -pvc modelagem01
view:
	evince modelagem01.pdf &
pdfrela:
	latexmk -pdf relacionamento01
	latexmk -c
	ls -la
previewrela:
	subl relacionamento01.tex
	evince relacionamento01.pdf
	latexmk -pdf -pvc relacionamento01
viewrela:
	evince relacionamento01.pdf