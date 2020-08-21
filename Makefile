TARGETS = black env test

.PHONY: $(TARGETS)

all:
	$(error Valid targets are: $(TARGETS))

black:
	find . -type f -name "*.py" | xargs black -l 132

env:
	conda create -y -n bomradarloop -c conda-forge black pillow pylint requests

test:
	pylint --rcfile=pylintrc $$(find . -type f -name "*.py" | tr "\n" " ")
