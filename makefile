_PHONY: venv unittest install uninstall clean

venv:
	python3 -m venv venv
	venv/bin/python3 -m pip install --upgrade pip
	venv/bin/python3 -m pip install -r requirements.txt

run:
	venv/bin/python3 src/pymaze.py

unittest:
	python3 -m unittest discover -v

install:
	venv/bin/python3 setup.py install

uninstall:
	venv/bin/python3 -m pip uninstall pymaze -y

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*pycache*" | xargs rm -rf
