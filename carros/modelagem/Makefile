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