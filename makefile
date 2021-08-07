#
# pynotes - (Python implementation of Standard Unix Notes)
#
# NOTESDIR now set in tests/.env for tests
#export NOTESDIR=/home/ian/pynotes/__testing__/notesdir
#export NOTESDIR=/home/ian/pynotes/__testing__/.notes

default:	test

env:
	@echo  NOTESDIR is set in the file tests/.env for testing
	@cat __testing__/notesdir/config

test: 	clean
        #clear
	@gpg --import tests/test.key tests/test.pub tests/alttest.key tests/alttest.pub
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

testoneattime:
	python -m unittest tests/test_backup.py
	read wait
	python -m unittest tests/test_config_functions.py
	read wait
	python -m unittest tests/test_dotenv.py
	read wait
	python -m unittest tests/test_encrypt_and_decrypt.py
	read wait
	python -m unittest tests/test_notebook_functions.py
	read wait
	python -m unittest tests/test_note_file_functions.py
	read wait
	python -m unittest tests/test_notes_class_init.py
	read wait
	python -m unittest tests/test_notes_set_text.py
	read wait
	python -m unittest tests/test_path_functions.py
	read wait
	python -m unittest tests/test_save_load_notes.py
	read wait
	python -m unittest tests/test_utility_functions.py
	read wait

coverage:
	coverage run -m unittest
	coverage html
	coverage report  -m

tree:
	tree -a __testing__

clean:
	-@rm -rf __testing__/*  __testing__/.*
	coverage erase
	-@rm -rf htmlcov

delete-gpg-testkeys:
	gpg --batch --yes --delete-secret-keys E4D4E23B3AC48FFA15C1949216427604C30E9831
	gpg --batch --yes --delete-keys E4D4E23B3AC48FFA15C1949216427604C30E9831
	gpg --batch --yes --delete-secret-keys 42456745CCBF000CA591E73CDBCC0C3D5CB54E7B
	gpg --batch --yes --delete-keys 42456745CCBF000CA591E73CDBCC0C3D5CB54E7B

cleaner: clean delete-gpg-testkeys


pip:
	pip install python-gnupg
	pip install pudb coverage black pylint 
	pip install python-dotenv

changelog:
	git2cl > ChangeLog

release_notes:
	reno report 

