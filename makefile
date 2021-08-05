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

pip:
	pip install python-gnupg
	pip install pudb coverage
	pip install python-dotenv

changelog:
	git2cl > ChangeLog

release_notes:
	reno report 
