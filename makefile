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

clean:
	@rm -rf __testing

compile:
	echo compile


pip:
	pip install configparser
	pip install python-gnupg	

