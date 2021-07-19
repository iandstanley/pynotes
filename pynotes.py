"""
PYNOTES the Python implementation of Standard Unix Notes

pynotes.py - (this file) implements the classes in a module to be loaded by the other executables.
notes.py    - command line tool for managing notes
notebook.py - command line tools for managing notebooks
gnotes.py   - co


"""



'''  FEATURES TO ADD:

- what init variations do i need
- create note
- import note
- edit note
- copy note
- move note
- delete note
- encrypt note
- decrypt note
- git status
- git commit
- git init (this should probably be in config
- git log
- git config 
- view note
- search notes
- new key for gpg
- backup notes
- tree of directory
- HELP 
'''

class config:
    '''Configuration object for pynotes
    '''
    def __init__(self):
        self.gpgkey="sdfghjkjhfghjjfghj"
        self.usegit="false"
        self.defaultnotebook="Notes"
        self.usenotebook="Notes"

        
    


class notes:
    '''
    Notes class for handling notes objects
    '''

    def __init__(self):
        self.testinit=True



class notebook:
    '''
    Notebook class for handling notebooks containing notes
    '''

    def __init__(self):
        self.testinit=True

