#
# pynotes - (Python implementation of Standard Unix Notes)
#
export NOTESDIR=/home/ian/pynotes/__testing__/notesdir

default:	test

help:
	echo help

test: 	clean
	mkdir -p $(NOTESDIR)
#	python -m unittest test_config.py	
#	python -m unittest test_notesystem.py	
#	python -m unittest test_notebook.py	
#	python -m unittest test_notes.py	
#	python -m unittest test_open.py	
	python -m unittest

debug:
	python -m pudb try_open.py

tree:
	tree -a $(NOTESDIR)
clean:
	@rm -rf __testing__

compile:
	echo compile


pip:
	pip install configparser
	pip install python-gnupg	

