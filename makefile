#
# pynotes - (Python implementation of Standard Unix Notes)
#

default:	test

help:
	echo help

test: 
	python -m unittest 	

compile:
	echo compile


pip:
	pip install configparser
	pip install gnupg	
