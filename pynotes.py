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
import os, shutil, datetime, tarfile, pathlib
import gnupg        # see https://docs.red-dove.com/python-gnupg/

from dumper import dump 

'''  FEATURES TO ADD:
X read/write config file
X create note
X import note
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
X backup notes
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
        self.home = os.environ['HOME']

        if git == False:
            self.usegit = False
        else:
            self.usegit = True

        # calculate NOTESDIR
        if 'XDG_DATA_DIR' in os.environ:
            self.notesdir =  os.environ['XDG_DATA_DIR']
        elif 'NOTESDIR' in os.environ:
            self.notesdir = os.environ['NOTESDIR']
        else:
            self.notesdir = self.home + "/.notes"

        self.configfile=f"{self.notesdir}/config"

##        print(f"os.environ = {os.environ['NOTESDIR']}")
##        print(f"config.notedir = {self.notesdir}     config.configfile = {self.configfile}")

 
        self.initran = True


    def setGPGkey(self, key):
        self.gpgkey = key

    def writeConfig(self):
        ''' write config to configfile
        '''
        c = ConfigParser()
        c[config.section] = {
            'key': self.gpgkey,
            'usegit': str(self.usegit),
            'spelling': self.spelling,
            'notesdir': self.notesdir, # not read from config file
            'configfile': self.configfile,
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

    def __init__(self,git=False):
        '''
        __init__ notessystem

        Git Initialisation:
            Specify notesystem(git=True) can be used to create a git repo
            inside the NOTESDIR. Commits will be made on each change
            The default is not to have a git repo ie. 'ns = notesystem()' .
        '''

        
        self.config = config(git=git)
        self.using = self.config.defaultnotebook
        self.default_fullpath = self.config.notesdir + '/' + self.config.defaultnotebook
        self.use_fullpath = self.config.notesdir + '/' + self.config.usenotebook        
        self.setupMissingDirs()

        # grab first private key for use by default
        self.config.setGPGkey(self.getDefaultGPGkey())

        if not os.path.isfile(self.config.configfile):
            self.config.writeConfig()

        self.initran = True

    def setupMissingDirs(self):
        
        if not os.path.isdir(self.config.notesdir):
            # TODO maybe log these print statements
            print(f"NOTESDIR does not exist, creating {self.config.notesdir}")
            os.mkdir(self.config.notesdir, mode=0o700)

        if not os.path.isdir(self.default_fullpath):
            print(f"Default notebook does not exist, creating {self.config.defaultnotebook}")
            os.mkdir(self.default_fullpath, mode=0o700)

        if not os.path.isdir(self.use_fullpath):
            # repetitous but just in case config file has been manually edited
            print(f"Setting the current notebook to {self.config.usenotebook}")
            os.mkdir(self.use_fullpath, mode=0o700)

    def getDefaultNotebook(self):
        return self.config.defaultnotebook

    def getUseNotebook(self):
        return self.config.usenotebook

    def getDefaultNotebookFullpath(self):
        return self.default_fullpath

    def getUseNotebookFullpath(self):
        return self.use_fullpath

    def getNotebooks(self):
        ''' Return a collection of all existing notebooks
        '''
        return [d for d in os.listdir(self.config.notesdir) if os.path.isdir(os.path.join(self.config.notesdir, d))]

    def getNotes(self,notebook):
        ''' Return a collection of all notes within a specified notebook
        '''
        return os.listdir(notebook.fullpath)    

    def backup(self):
        ''' backup notes to file
        '''
        t = datetime.datetime.now()
        backupfile = f"{self.config.notesdir}/../notes_backup_{t.strftime('%Y%b%d_%H%M')}.tar"

        try:
            tar = tarfile.open(backupfile,'w')
            tar.add(self.config.notesdir)
            tar.close()
            return True
        
        except tar.TarError as err:
            return err

        
    def newKey(self, key):
        '''
        Change GPG key for all notes.

        This takes a GnuPG keyId as a parameter.
        The key is validated as a private key on the user's keyring before processing
        '''
        if not self.validateGPGkey(key):    # return False if not valid private key
            return False
        

        # then process each file and decrypt/encrypt them

        # update config file with new GPG key
    

        return True


    def validateGPGkey(self,key):
        ''' Validates that the supplied key is a PRIVATE key
        '''
        gpg = gnupg.GPG(gnupghome=self.gnupghome)
        if gpg.list_keys(True,keys=key):
            return True
        else:
            return False
        
    def getDefaultGPGkey(self):
        ''' Return default GPG private key
        Returns the first private key in our keyring
        '''
        self.gnupghome = self.config.home + '/.gnupg'
        self.gpg = gnupg.GPG(gnupghome=self.gnupghome)
        self.private_keys = self.gpg.list_keys(True) # True => private key
        return self.private_keys[0]['keyid']     # get first key



#==================================#
                                                   
class notes:
    '''
    Notes class for handling notes objects
    '''

    def __init__(self):
        self.config = config()
        self.config.readConfig()
        self.testinit=True
        self.plaintext = ''
        self.ciphertext = ''
        self.notebook = ''
        self.notetitle = ''
        self.notefullpath = ''

    def create(self, title):
        ''' add a note
        '''
        title = title.replace(" ","_")
        titlepath = self.prependUseNotebook(title)
        
        if os.path.exists(titlepath):
            return False

        self.notetitle = title
        self.notefullpath = titlepath

##        with open(self.notefullpath, 'w') as nf:
##            nf.write('')    # touch notefile
##            nf.close()
        
        return self

    def open(self, filename):
        ''' add a note
        '''
        titlepath = self.prependUseNotebook(filename)

        ftitle, fext = os.path.splitext(filename)
        
        if not os.path.exists(titlepath):
            return False

        self.notetitle = ftitle
        self.notefullpath = titlepath

        with open(self.notefullpath, 'r') as nf:
            textcontent = nf.read()
            nf.close()

        if fext == '.asc':
            self.ciphertext = textcontent
            self.plaintext = ''
        else:
            self.ciphertext = ''
            self.plaintext = textcontent


    def setPlaintext(self,PT):
        ''' Save PT parameter to object
        '''
        self.plaintext = PT

    def setCiphertext(self,CT):
        ''' Save CT parameter to object
        '''
        self.ciphertext = CT

    def saveCiphertext(self):
        ''' Save CT to file
        '''
        with open(self.prependUseNotebook(self.notetitle+'.asc'), 'w') as outp:
            outp.write(self.ciphertext)

    def savePlaintext(self):
        ''' Save PT to file
        '''
        with open(self.prependUseNotebook(self.notetitle), 'w') as outp:
            outp.write(self.plaintext)
 
    def importNote(self, filename):
        ''' import a note from a file
        '''
        if not os.path.exists(filename):
            return False
            
        with open(filename, 'r') as imp:
            self.plaintext = imp.read()
            self.notetitle = filename.replace(" ","_")
            self.notefullpath = self.prependUseNotebook(filename)

            imp.close()
##    TODO: encrypt and save

        # encrypt

        # save note


    def rename(self, newname):
        ''' rename a note
        '''
        newname = self.prependUseNotebook(newname.replace(" ","_"))
        
        if not os.path.exists(self.prependUseNotebook(self.notetitle)):
            return False

        shutil.move(self.prependUseNotebook(self.notetitle), newname)

        return os.path.exists(newname)


    def duplicate(self, newname):
        ''' duplicate a note
        '''
        newname = self.prependUseNotebook(newname.replace(" ","_"))
        
        if not os.path.exists(self.prependUseNotebook(self.notetitle)):
            return False

        shutil.copy2(self.prependUseNotebook(self.notetitle), newname)

        return os.path.exists(newname)


    def delete(self):
        ''' delete note
        '''
##        title = title.replace(" ","_")
        pass
    
    def copyTo(self, notebook):
        ''' copy a note to another notebook
        '''
        newname = self.prependAnotebook(notebook, self.notetitle)
        if os.path.exists(newname):
            return False

        shutil.copy2(self.prependUseNotebook(self.notetitle), newname)

        return os.path.exists(newname)


    def moveTo(self, notebook):
        ''' move a note to new notebook
        '''
        newname = self.prependAnotebook(notebook, self.notetitle)
        
        if not os.path.exists(self.prependUseNotebook(self.notetitle)):
            return False

        shutil.move(self.prependUseNotebook(self.notetitle), newname)

        return os.path.exists(newname)



    def encrypt(self):
        ''' encrypt Plaintext to Ciphertext
        '''
        # dummy encryption
        self.ciphertext = "%% " + self.plaintext
        self.plaintext = ''
##        print(f"encrypt(): ciphertext = {self.ciphertext}")

    
    def decrypt(self):
        ''' encrypt Plaintext to Ciphertext
        '''
        self.plaintext = self.ciphertext[3:]
        self.ciphertext = ''
##        print(f"decrypt(): plaintext = {self.plaintext}")

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

    def prependUseNotebook(self, title):
        ''' prepend fullpath of file
        Add the current self.usenotebook fullpath
        '''
        return f"{self.config.notesdir}/{self.config.usenotebook}/{title}"

    def prependAnotebook(self, notebook, title):
        ''' prepend fullpath of file
        Add the current self.usenotebook fullpath
        '''
        return f"{self.config.notesdir}/{notebook}/{title}"


#==================================#

class notebook:
    '''
    Notebook class for handling notebooks containing notes
    '''

    def __init__(self):
        self.config = config()
        self.config.readConfig()
        self.notebookname = ''
        self.notebookpath = ''
        
        self.testinit=True

    def create(self, title):
        ''' creates a new notebook directory under the NOTESDIR
        notebook().create(title)
        Replaces spaces with underscores in title
        '''
        self.notebookname = title.replace(" ","_")
        self.notebookpath = self.config.notesdir + '/' + self.notebookname

        if not os.path.exists(self.notebookpath):
            os.mkdir(self.notebookpath, mode=0o700)

        return os.path.exists(self.notebookpath)
        
    def rename(self, title):
        ''' rename a notebook
        Renames existing notebook as title
        '''
        title = title.replace(" ","_")
        frompath = self.notebookpath
        topath = self.config.notesdir + '/' + title

        if os.path.exists(self.notebookpath):
            os.rename(frompath, topath)
            self.notebookpath = topath

        return os.path.exists(self.notebookpath)


    def duplicate(self, title):
        ''' duplicate a notebook
        '''
        title = title.replace(" ","_")
        frompath = self.notebookpath
        topath = self.config.notesdir + '/' + title

        if os.path.exists(frompath) and not os.path.exists(topath):
            shutil.copytree(frompath,topath)
        return os.path.exists(topath)
    
    def delete(self):
        ''' delete notebook and notes
        '''
        if os.path.exists(self.notebookpath):
            shutil.rmtree(self.notebookpath)
        return not os.path.exists(self.notebookpath)
        
    def use(self,title):
        ''' use notebook
        '''
        title = title.replace(" ","_")
        n = self.config.notesdir + '/' + title
        if os.path.exists(self.config.notesdir + '/' + title):
            self.notebookname = title
            self.notebookpath = self.config.notesdir + '/' + self.notebookname
            self.config.usenotebook = title
        return

    def default(self):
        ''' switch back to default notebook
        '''
        self.config.usenotebook = self.config.defaultnotebook


#==================================#

if __name__ == "__main__":

    pass
