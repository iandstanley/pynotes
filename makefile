#
# pynotes - (Python implementation of Standard Unix Notes)
#

default:	test

help:
	echo help

test: 
	#	python -m unittest 	
		python -m unittest test_config
	#	python -m unittest test_notesystem

compile:
	echo compile


pip:
	pip install configparser
	#pip install unittest2
	
