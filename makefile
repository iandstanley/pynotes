#
# pynotes - (Python implementation of Standard Unix Notes)
#
export NOTESDIR=__testing__/notesdir

default:	test

help:
	echo help

test: 	clean
	mkdir -p $(NOTESDIR)
	python -m unittest 	

tree:
	tree -a $(NOTESDIR)
clean:
	@rm -rf __testing__

compile:
	echo compile


pip:
	pip install configparser
	pip install python-gnupg	

