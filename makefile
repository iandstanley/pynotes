#
# pynotes - (Python implementation of Standard Unix Notes)
#
#export NOTESDIR=/home/ian/pynotes/__testing__/notesdir
export NOTESDIR=/home/ian/pynotes/__testing__/.notes

default:	test

help:
	echo help

test: 	clean
        #clear
	echo "NOTESDIR in makefile reads = $(NOTESDIR) "
	mkdir -p $(NOTESDIR)
	python -m unittest -v tests/*.py
	@if [ $$? -eq 0 ]; then \
	   coverage report -m ; \
	fi

debug:
	python -m pudb tests/test_config.py

coverage:
	coverage run -m unittest 
	coverage report  -m

tree:
	tree -a __testing__

config_show:
	cat $(NOTESDIR)/config 


clean:
	@rm -rf __testing__/*

compile:
	echo compile


pip:
	pip install configparser
	pip install python-gnupg	

changelog:
	git2cl > ChangeLog

release_notes:
	reno report 
