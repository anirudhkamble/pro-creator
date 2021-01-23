
install:
	python setup.py install

build:
	python setup.py build

clean:
	rm -rf build
	rm -rf dist
	rm -rf ./src/*.egg-info

