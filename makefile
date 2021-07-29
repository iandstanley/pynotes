#
# pynotes - (Python implementation of Standard Unix Notes)
#
export NOTESDIR=/home/ian/pynotes/__testing__/notesdir

default:	test

help:
	echo help

test: 	clean
	mkdir -p $(NOTESDIR)
	#	python -m unittest tests/*.py
	python -m unittest tests/test_config.py

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

changelog:
	git2cl > ChangeLog

release_notes:
	reno report 
