#
# pynotes - (Python implementation of Standard Unix Notes)
#
export NOTESDIR=/home/ian/pynotes/__testing__/notesdir
#export NOTESDIR=/home/ian/pynotes/__testing__/.notes

default:	test

env:
	@echo  NOTESDIR is set to $(NOTESDIR)

test: 	clean
        #clear
	echo "NOTESDIR in makefile reads = $(NOTESDIR) "
	mkdir -p $(NOTESDIR)
	#python -m unittest -v tests/*.py
	coverage run -m unittest
	coverage html
	@if [ $$? -eq 0 ]; then \
	   coverage report -m ; \
	fi

debug:
	python -m pudb tests/test_config.py

coverage:
	coverage run -m unittest
	coverage html
	coverage report  -m

morecoverage:
	coverage run -m unittest  -v 2
	coverage report  -m

tree:
	tree -a __testing__

config_show:
	cat $(NOTESDIR)/config 


clean:
	rm -rf __testing__/*
	coverage erase
	rm -rf htmlcov

compile:
	echo compile


pip:
	pip install configparser
	pip install python-gnupg	

changelog:
	git2cl > ChangeLog

release_notes:
	reno report 
