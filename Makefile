pdf:
	latexmk -pdf --shell-escape django
	latexmk -c
preview:
	evince django.pdf &
	latexmk -pdf --shell-escape -pvc django