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
	@gpg --import tests/test.key tests/test.pub tests/alttest.key tests/alttest.pub
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
	gpg --batch --yes --delete-secret-keys E4D4E23B3AC48FFA15C1949216427604C30E9831
	gpg --batch --yes --delete-keys E4D4E23B3AC48FFA15C1949216427604C30E9831
	gpg --batch --yes --delete-secret-keys 42456745CCBF000CA591E73CDBCC0C3D5CB54E7B
	gpg --batch --yes --delete-keys 42456745CCBF000CA591E73CDBCC0C3D5CB54E7B

cleaner: clean delete-gpg-testkeys


pip:
	pip install python-gnupg
	pip install pudb coverage
	pip install python-dotenv

changelog:
	git2cl > ChangeLog

release_notes:
	reno report 

