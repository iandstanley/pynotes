#
# pynotes - (Python implementation of Standard Unix Notes)
#
# NOTESDIR now set in tests/.env for tests
#export NOTESDIR=/home/ian/pynotes/__testing__/notesdir
#export NOTESDIR=/home/ian/pynotes/__testing__/.notes

default:	test

env:
	@echo  NOTESDIR is set in the file tests/.env for testing
	@cat $(NOTESDIR)/config

test: 	clean
        #clear
	@gpg --import tests/testkey* tests/alttestkey* 2>/dev/null
	@echo "NOTESDIR in makefile reads = $(NOTESDIR) "
	mkdir -p $(NOTESDIR)
	#python -m unittest -v tests/*.py
	coverage run -m unittest
	@coverage html
	@if [ $$? -eq 0 ]; then \
	   coverage report -m ; \
	fi

debug:
	python -m pudb tests/test_notes.py

coverage:
	coverage run -m unittest
	coverage html
	coverage report  -m

tree:
	tree -a __testing__

clean:
	rm -rf __testing__/*
	coverage erase
	rm -rf htmlcov

delete-gpg-testkeys:
	gpg --batch --yes --delete-secret-keys 8A7E27118BE62DB9C94AFCD5B430CA1D89D91672
	gpg --batch --yes --delete-keys 8A7E27118BE62DB9C94AFCD5B430CA1D89D91672
	gpg --batch --yes --delete-secret-keys EBE9A06A2D15C4229F549D97A6D26EFA64C588D0
	gpg --batch --yes --delete-keys EBE9A06A2D15C4229F549D97A6D26EFA64C588D0

cleaner: clean delete-gpg-testkeys


pip:
	pip install python-gnupg
	pip install pudb coverage
	pip install python-dotenv

changelog:
	git2cl > ChangeLog

release_notes:
	reno report 

