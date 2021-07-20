"""
PYNOTES the Python implementation of Standard Unix Notes

pynotes.py - (this file) implements the classes in a module to be loaded by the other executables.
notes.py    - command line tool for managing notes
notebook.py - command line tool for managing notebooks
gnotes.py   - gui tool for managing notebooks and notes

The following classes are implemented:

    config     - Manages the application configuration reads/writes to config file
    notesystem - Handles application wide things like changing keys and backup
    note       - notes related stuff
    notebook   - notebook related stuff

"""

from configparser import ConfigParser 
import os
import dumper

'''  FEATURES TO ADD:
X read/write config file
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
    '''
    Configuration object for pynotes

    The configuration file 'config' is found in the root
    of the NOTESDIR.

    The following configuration parameters are found there:

        key      - GPG private key used to decrypt notes
        usegit   - Use git repo and commiting changes 'true'/'false'
        spelling - Choose from 'aspell', 'ispell' or 'None'

    '''
    section = 'DEFAULT'

    def __init__(self,git=False):
        self.gpgkey="DummyGpgKey"
        self.spelling="None"
        self.defaultnotebook="Notes"
        self.usenotebook="Notes"
        self.configfile="config.ini"
        self.home = os.environ['HOME']

        if git == False:
            self.usegit = False
        else:
            self.usegit = True

        # calculate NOTESDIR
        if 'XDG_DATA_DIR' in os.environ:
            notesdir =  os.environ['XDG_DATA_DIR']
        elif 'NOTESDIR' in os.environ:
            notesdir = os.environ['NOTESDIR']
        else:
            notesdir = self.home + "/.notes"

        self.initran = True


    def writeConfig(self):
        ''' write config to configfile
        '''
        c = ConfigParser()
        c[config.section] = {
            'key': self.gpgkey,
            'usegit': str(self.usegit),
            'spelling': self.spelling,
            'usenotebook': self.usenotebook,
            'defaultnotebook': self.defaultnotebook   
        }

        with open(self.configfile, 'w') as configfile:
            c.write(configfile)

    def readConfig(self):
        ''' read config from configfile
        '''
        c = ConfigParser()
        c.read(self.configfile)

        self.gpgkey = c[config.section]['key']
        self.usegit = bool(c[config.section]['usegit'] == "True")
        self.spelling = c[config.section]['spelling']
        self.usenotebook = c[config.section]['usenotebook']
        self.defaultnotebook = c[config.section]['defaultnotebook']


#==================================#


class notesystem:

    def __init__(self):

        self.config = config()

        self.using = self.config.defaultnotebook
        

        # if default/use notebooks do not exist create

        self.initran = True
        
    def newKey(self, key):
        ''' change GPG key for all notes
        '''
        return true

    def backup(self):
        ''' backup notes to file
        '''
        return true

    def getKeyring(self):
        pass

    def getFirstGPGKey(self):
        pass

#==================================#
                                                   
class notes:
    '''
    Notes class for handling notes objects
    '''

    def __init__(self):
        self.testinit=True

    def add(self, title):
        ''' add a note
        '''
        pass

    def importNote(self, filename):
        ''' import a note from a file
        '''
        pass

    def rename(self, filename, newname):
        ''' rename a note
        '''
        pass

    def duplicate(self, filename, newfilename):
        ''' duplicate a note
        '''
        pass

    def delete(self):
        ''' delete note
        '''
        pass
    
    def copyTo(self, filename, newfilename):
        ''' copy a note to another notebook
        '''
        pass

    def moveTo(self, filename, notebook):
        ''' move a note to new notebook
        '''
        pass

    def encrypt(self):
        ''' encrypt Plaintext to Ciphertext
        '''
        pass

    def decrypt(self):
        ''' encrypt Plaintext to Ciphertext
        '''
        pass

    def save(self):
        ''' save note
        '''
        pass

    def saveAs(self, filename):
        ''' save as note with new filename
        '''
        pass

    def view(self):
        ''' view note
        '''
        pass

    def edit(self):
        ''' edit note
        '''
        pass

#==================================#

class notebook:
    '''
    Notebook class for handling notebooks containing notes
    '''

    def __init__(self):
        self.testinit=True


    def add(self, title):
        ''' add a notebook
        '''
        pass

    def rename(self, newname):
        ''' rename a notebook
        '''
        pass

    def duplicate(self, newfilename):
        ''' duplicate a notebook
        '''
        pass
    
    def delete(self):
        ''' delete notebook and notes
        '''
        pass

    def use(self,notebook):
        ''' use notebook
        '''
        pass

    def default(self):
        ''' switch back to default notebook
        '''
        pass


#==================================#

if __name__ == "__main__":

    pass
