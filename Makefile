
.PHONY: all
all: tests doc dist

.PHONY: tests
tests: 
	tox
	#py.test -v --doctest-glob *.rst
	#py.test -v --doctest-modules yamltempl

.PHONY: pep8
pep8: yamltempl
	pep8 yamltempl

.PHONY: cheesecake
cheesecake: dist
	cheesecake_index -p dist/yamltempl*.tar.gz

.PHONY: dist
dist: setup.py yamltempl
	python setup.py sdist

#TODO prepare docs to be distributed
.PHONY: doc
doc:
	$(MAKE) -C docs html

.PHONY: clean
clean: clean_temp clean_compiled
	$(MAKE) -C docs clean
	-rm -rf dist
	-rm MANIFEST

.PHONY: clean_temp
clean_temp:
	-find . -name '*~' | xargs rm -f

.PHONY: clean_compiled
clean_compiled:
	-find * -name '*.pyc' | xargs rm -f
