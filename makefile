_PHONY: install uninstall clean

install:
	python3 setup.py install

uninstall:
	pip3 uninstall pymaze -y

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*pycache*" | xargs rm -rf
