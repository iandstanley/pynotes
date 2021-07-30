#
# pynotes - (Python implementation of Standard Unix Notes)
#
#export NOTESDIR=/home/ian/pynotes/__testing__/notesdir
export NOTESDIR=/home/ian/pynotes/__testing__/.notes

default:	test

help:
	echo help

test: 	clean
	mkdir -p $(NOTESDIR)
	clear
	python -m unittest tests/test_initdirs.py
	python -m unittest -v test_config.py

debug:
	python -m pudb test_config.py

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
