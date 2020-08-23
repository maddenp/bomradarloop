TARGETS = black dist env gifs test upload

.PHONY: $(TARGETS)

all:
	$(error Valid targets are: $(TARGETS))

black:
	find . -type f -name "*.py" | xargs black -l 132

dist:
	python setup.py sdist bdist_wheel

gifs:
	python fetchall.py

env:
	conda create -y -n bomradarloop -c conda-forge black pillow pylint requests twine

test:
	pylint --rcfile=pylintrc $$(find . -type f -name "*.py" | tr "\n" " ")

upload: dist
	python -m twine upload --repository pypi dist/*
