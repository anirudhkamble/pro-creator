
.PHONY: tests

install:
	python setup.py install

build:
	python setup.py build

tests:
	python -m unittest discover tests -v

clean:
	rm -rf build
	rm -rf dist
	rm -rf ./src/*.egg-info
