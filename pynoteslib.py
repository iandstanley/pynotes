"""
PYNOTESLIB the Python library implementation of Standard Unix Notes

PYNOTESLIB  implements the notes() class and a number of functions to manipulate notebooks

"""

from configparser import ConfigParser
import toml
import os
import shutil
import datetime
import tarfile
import gnupg  # see https://docs.red-dove.com/python-gnupg/

_default_config = {
    "gpgkey": "",
    "spelling": "none",
    "default": "Notes",
    "use": "Notes",
    "home": os.environ["HOME"],
    "notesdir": "",
    "configfile": "",
    "usegit": False
}

GPGEXT = '.asc'

def _init_dirs():
    """
    init_dirs()     function to setup the NOTESDIR directory structure

    This function is meant to be used internally by the module
    _init_dirs() is called by create_config()

    1.  This function gets the base NOTESDIR from get_notedir() which in
        turn examines the environment variable for $NOTESDIR else uses ~/.notes
    2.  Creates $NOTESDIR directory
    3.  Creates first Notebook '$NOTESDIR/Notes/'

    :param none:
    :return none:
    """
    notesdir = get_notesdir()

    if not os.path.isdir(notesdir):
        os.mkdir(notesdir, mode=0o700)

    if not os.path.isdir(notesdir + "/Notes"):
        print(f"Default notebook does not exist, creating {notesdir + '/Notes'}")
        os.mkdir(notesdir + "/Notes", mode=0o700)

def create_config():
    """
    create_config()     function is used to setup the notes directory structure under $NOTESDIR
                        and TOML config file $NOTESDIR/config
    :param none:
    :return none:
    """
    _init_dirs()         # setup directory structure if needed
    conf = dict(_default_config)

    conf["notesdir"] = get_notesdir()
    conf["configfile"] = get_config_file()
    conf["gpgkey"] = get_default_gpg_key()

    write_config(conf)

def get_config():
    """
    get_config()    function reads configuration from the TOML file $NOTESDIR/config
                    If 'config' file does not exist, calls create_config() to create
    :param none:
    :return configuration:  Returns the dict loaded from the TOML file 'config'
    """

    if config_file_exists():
        with open(get_config_file(), "r") as f:
            return toml.load(f)
    else:
        create_config()

def write_config(conf):
    """
    write_config(conf)  function dumps app configuration to TOML file $NOTESDIR/config
    :param conf:        Dictionary containing configuration
                        (see_default_config as a sample structure)
    :return bool:       returns True on successful write of configfile
    """
    # write config to config file
    # TODO write error handler for
    with open(get_config_file(), "w") as configf:
        toml.dump(conf, configf)
        return True

def get_config_file():
    """
    get_config_file()   function returns fullpath to the app configuration file
    :return str:        returns the config file fullpath as a string
    """
    return get_notesdir() + "/config"

def get_notesdir():
    """
    get_notesdir()      function returns fullpath to the main app directory

    :param none:
    :return str:        returns the app's home folder (either $NOTESDIR or $HOME/.notes)
    """

    if "NOTESDIR" in os.environ:
        notesdir = os.environ["NOTESDIR"]
    else:
        notesdir = os.environ["HOME"] + "/.notes"

    return notesdir

def config_file_exists():
    """
    config_file_exists()    function checks to see if $NOTESDIR/config file exists
    :return bool:
    """
    return os.path.exists(get_config_file())

def use_git():
    """
    use_git()       Checks to see if we are using git to manage $NOTESDIR/
    :return bool:   True if configuration is set to use git for commits when saving notes
    """
    conf =  get_config()
    return conf['usegit']

def set_git(gitstatus):
    """
    set_git(bool gitstatus)     function sets whether to use git commits when saving notes
                                and updates the config file accordingly
    :param bool:        Uses boolean parameter to update configuration
    :return dict:       returns the latest config
    """
    conf =  get_config()
    conf['usegit'] = gitstatus
    write_config(conf)
    return conf

def get_default_gpg_key():
    """
    get_default_gpg_key()       finds the first private key in the users GPG keyring
    :return key:    returns the GPG key ID of the first private GPG key found in users keyring
    """
    return "gpg_key_default"


def backup(conf):
    """
    backup()                Backup configuration, notes and notebook to tar file
    :return:
    """
    # TODO Fixup to work after refactoring
    t = datetime.datetime.now()
    backupfile = (
        f"{notesdir}/../notes_backup_{t.strftime('%Y%b%d_%H%M')}.tar"
    )

    try:
        tar = tarfile.open(backupfile, "w")
        tar.add(notesdir)
        tar.close()
        return True

    except tar.TarError as err:
        return err

def get_default_notebook():
    """
    get_default_notebook()          Reads config file and returns what notebook is the default
    :return:
    """
    conf = get_config()
    return conf['default']

def get_use_notebook():
    """
    get_use_notebook()      Reads config file and returns what notebook is currently used notebook
    :return str:            returns the currently 'use'd notebook (where notes will be created)
    """
    conf = get_config()
    return conf['use']

def default_notebook(nb):
    """
    default_notebook()      Set the default notebook (which use_notebook defaults to if given '' instead of a notebook title)
    :return bool:           returns bool re success.
    """
    conf = get_config()
    nb_fullpath = get_fullpath(nb)

    if os.path.exists(nb_fullpath):
        conf['default'] = nb

    return write_config(conf)

def use_notebook(nb):
    """
    use_notebook()  Reads config file and returns what notebook is the default
    :return bool:           returns bool re success.
    """
    conf = get_config()
    nb_fullpath = get_fullpath(nb)

    if os.path.exists(nb_fullpath):
        conf['use'] = nb

    return write_config(conf)

def get_notebooks():
    """
    get_notebooks()         Returns a list of all notebooks in NOTESDIR
    :return list:
    """
    conf = get_config()
    return next(os.walk(conf['notesdir']))[1]

def get_notes(self, notebook=''):
    """
    get_notes()                 Returns a list of note in given notebook (or the USE'd notebook if none supplied)
    :param self:
    :param (optional) notebook: Specify notebook or default to the USE'd notebook
    :return:
    """
    if notebook == '':
        conf = get_config()
        notebook = conf['use']

    notebook = os.path.join(get_notesdir(), notebook)

    return os.listdir(notebook)

"""
def new_key(self, key):
    #     Change GPG key for all notes.

    if not self.validate_gpg_key(key):  # return False if not valid private key
        return False

    # then process each file and decrypt/encrypt them

    # update config file with new GPG key

    return True

def validate_gpg_key(self, key):
    #Validates that the supplied key is a PRIVATE key
    gpg = gnupg.GPG(gnupghome=self.gnupghome)
    if gpg.list_keys(True, keys=key):
        return True
    else:
        return False

"""

def get_fullpath(name):
    """
    get_fullpath(name)          Return full pathname of passed parameter
    :param name:                A directory (Notebook), filename ('config' file) or expression ('WorkNotebook' + filename)
    :return str:                Returns the full path in the filesystem for 'name' UNDER the NOTESDIR
    """
    conf = get_config()
    return conf['notesdir'] + '/' + name

def get_note_fullpath(note):
    """
    get_use_fullpath(note)      Returns the full pathname of a note within the currently USE'd Notebook
    :param note:                title (or filename) of a note
    :return str:                Returns full path to a no
    """
    conf = get_config()
    return conf['notesdir'] + '/' + conf['use'] + '/' + change_spaces(note)

def change_spaces(str):
    return str.replace(" ", "_")

# ================ notebook functions ==================#

def create_notebook(title):
    #conf = get_config()
    notebookname = title.replace(" ", "_")
    notebookpath = get_fullpath(title)

    if not os.path.exists(notebookpath):
        os.mkdir(notebookpath, mode=0o700)

    return os.path.exists(notebookpath)

def rename_notebook(oldtitle, newtitle):
    """rename a notebook
    Renames existing notebook as title
    """
    frompath = get_fullpath(change_spaces(oldtitle))
    topath = get_fullpath(change_spaces(newtitle))

    if os.path.exists(frompath):
        os.rename(frompath, topath)

    return os.path.exists(topath)

def duplicate_notebook(oldtitle, newtitle):
    """duplicate a notebook"""
    frompath = get_fullpath(change_spaces(oldtitle))
    topath = get_fullpath(change_spaces(newtitle))

    if os.path.exists(frompath) and not os.path.exists(topath):
        shutil.copytree(frompath, topath)
    return os.path.exists(topath)

def delete_notebook(title):
    """delete notebook and notes"""
    #conf = get_config()
    # title = title.replace(" ", "_")
    notebookpath = get_fullpath(change_spaces(title))

    if os.path.exists(notebookpath):
        shutil.rmtree(notebookpath)
    return not os.path.exists(notebookpath)

# ================= Note helper functions =================#

def import_note(filename):
    """
    import_note()       Creates a note from a file assigning to plaintext or
                        ciphertext depending on file extension

    :param filename:    fullpath of filename
    :return note:       returns an object of class note containing contents of file
    """
    if os.path.exists(filename):

        mynote = Notes(filename)
        _title, _ext = os.path.splitext(mynote.filename)

        if _ext == GPGEXT:

            # load cyphertext
            with open(mynote.filename, "r") as outp:
                mynote.ciphertext = outp.read()
                mynote.plaintext = ''

        else:
            # load plaintext
            with open(mynote.title, "r") as outp:
                mynote.plaintext = outp.read()
                mynote.ciphertext = ''

        outp.close()

        return mynote

def rename_note(oldname, newname):
    """
    rename_note()               Renames a note on disk inside the currently USE'd notebook
    :param oldname:             A string containing the old filename for note
    :param newname:             A string containing the new filename for note
    :return bool:               Success or failure
    """

    oldname = os.path.splitext(oldname)[0]
    newname = os.path.splitext(newname)[0]

    oldname = get_note_fullpath(oldname) + GPGEXT
    newname = get_note_fullpath(newname) + GPGEXT

    if not os.path.exists(oldname):
        return False

    shutil.move(oldname, newname)

    return os.path.exists(newname)

def duplicate_note(oldname, newname):
    """
    duplicate_note(newname)     Duplicates an encrypted note on disk inside the currently USE'd notebook
    :param newname:             A string containing the new filename for note
    :return bool:               Success or failure
    """
    oldname = os.path.splitext(oldname)[0]
    newname = os.path.splitext(newname)[0]

    oldname = get_note_fullpath(oldname) + GPGEXT
    newname = get_note_fullpath(newname) + GPGEXT

    if not os.path.exists(oldname):
        return False


    shutil.copy2(oldname, newname)

    return os.path.exists(newname)

def delete_note(filename):
    """
    delete_note()               Deletes a note on disk inside the currently USE'd notebook
    :param filename:            A string containing the filename of note to be deleted
    :return bool:               Success or failure
    """
    # TODO write method
    #        title = title.replace(" ","_")
    filename = get_note_fullpath(os.path.splitext(filename)[0] + GPGEXT)

    os.remove(filename)

    return os.path.exists(filename)

def copy_to_notebook(filename, notebook):
    """
    copy_to_notebook()          Copies note from current USE'd notebook to another notebook
    :param filename:            A string containing the filename of note to be copied
    :param notebook:            A string containing the target notebook name
    :return bool:               Success or failure
    """
    note = get_note_fullpath(os.path.splitext(filename)[0] + GPGEXT)
    notebook = os.path.join(get_notesdir(), os.path.splitext(notebook)[0])

    if not os.path.exists(note) or not os.path.exists(notebook):
        return False

    if not os.path.exists(os.path.splitext(notebook)[0]):
        return False

    shutil.copy2(note, notebook)

    return os.path.exists(notebook + note)

def move_to_notebook(filename, notebook):
    """
    move_to_notebook()          Moves a note from the currently USE'd notebook to another notebook
    :param filename:            A string containing the filename to move
    :param notebook:            A string containing the target notebook name
    :return bool:               Success or failure
    """
    filename = os.path.splitext(filename)[0] + GPGEXT
    note = get_note_fullpath(filename)
    notebook = os.path.join(get_notesdir(), os.path.splitext(notebook)[0])

    if not os.path.exists(note) or not os.path.exists(notebook):
        return False

    if not os.path.exists(os.path.splitext(notebook)[0]):
        return False

    os.rename(note, os.path.join(notebook, filename))

    return os.path.exists(os.path.join(notebook, filename))


class Notes:
    """
    class Notes:        Notes class for handling notes objects

    Attributes:
                title   title of note
                filename            filename of note. If specified at object creation,
                                    the instance will load from the specified filename
                                    from inside the USE'd notebook
                ciphertext          string containing the ciphertext of note
                plaintext           string containing the plaintext of note

                NB only one of either ciphertext or plaintext should be set at any time.
                Use set_plaintext() or set_ciphertext methods to ensure the other is set to ''

                _ftitle, _fext      filename and extension used internally in object creation only
                                    and not intended for application use as they are not updated
    Methods:
            __init__()              Instantiates object of type note: optional parameters
                                    see __init__() for details of valid constructor uses

            set_plaintext(str)      sets plaintext to string and ciphertext to ''
            set_ciphertext(str)     sets plaintext to '' and ciphertext to string

            save_ciphertext()       save ciphertext to file named self.filename + '.asc'
                                    in currently USE'd notebook
            save_plaintext()       save plaintext to file named self.filename
                                    in currently USE'd notebook

            load_note()             loads the contents of self.filename into note
            load_ciphertext()       handler for load_note() for filenames with extension .asc
            load_plaintext()        handler for load_note() for filenames without extension .asc

            encrypt()               encrypt note clearing plaintext
            decrypt()               decrypt note clearing ciphertext
    """


    def __init__(self, title='', plaintext='', ciphertext='', filename=''):
        """
        __init__(self, title='', plaintext='', ciphertext='', filename='')  class constructor

        To __init__() choose from the following optional parameters:
        :param str title:           a title for note - filename will be derived from title if given
        :param str plaintext:
        :param str ciphertext:
        :param str filename:        actual filename of file () including extension,
                                    data will be restored from the file called filename
                                    from the current USE'd notebook

        Valid constructors:
            Note()
            Note(title='my title')
            Note(title='my title', plaintext='this is the plaintext')
            Note(title='my title', ciphertext='<cipher text in ascii encoded gpg format>')
            Note(filename='my note filename.asc')
            Note(filename='my note filename')

        NB:     Features like editing a note should be handled by the app that uses this library
                eg. create a note or load it, decrypt it then edit the self.plaintext
                    before encrypting and saving again
        """
        self.testinit = True
        self.title = change_spaces(title)
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.filename = change_spaces(filename)

        if self.filename == '' and not self.title == '':
            self.set_filename(self.title)

        if self.get_extension() == '' and not self.ciphertext == '':
            self.add_extension()

        # if filename given process file
        if not self.filename == '':
            self._ftitle, self._fext = os.path.splitext(self.filename)
            self.load_note(self.filename)

    def add_extension(self):
        self.filename = os.path.splitext(self.filename)[0] + '.asc'

    def remove_extension(self):
        self.filename = os.path.splitext(self.filename)[0]

    def get_extension(self):
        return os.path.splitext(self.filename)[1]

    def set_filename(self, name):
        self.filename = change_spaces(name)

    def get_filename(self):
        return self.filename

    def set_plaintext(self, pt):
        """
        set_plaintext(pt)           Sets self.plaintext = pt & self.ciphertext = ''
        :param pt:                  String containing plaintext
        :return none:
        """
        """Save PT parameter to object"""
        self.plaintext = pt
        self.ciphertext = ''

    def set_ciphertext(self, ct):
        """
        set_ciphertext(ct)          Sets self.ciphertext = ct & self.plaintext = ''
                                    also adds the .asc to filename
        :param ct:
        :return:
        """
        """Save CT parameter to object"""
        self.ciphertext = ct
        self.plaintext = ''
        self.add_extension()

    def save_ciphertext(self):
        """
        save_ciphertext()           Saves Ciphertext of note to file named self.filename
        :return:
        """

        if self.filename == '':
            self.set_filename(self.title + '.asc')
        else:
            self.set_filename(os.path.splitext(self.filename)[0] + '.asc')

        # TODO add exception handling
        with open(get_note_fullpath(self.filename), "w") as outp:
            outp.write(self.ciphertext)

        outp.close()

    def save_plaintext(self):
        """
        save_plaintext()           Saves plaintext of note to file named self.filename
        :return:
        """
        if self.filename == '':
            self.set_filename(self.title)
        else:
            self.set_filename(os.path.splitext(self.filename)[0])

        # TODO add exception handling
        with open(get_note_fullpath(self.title), "w") as outp:
            outp.write(self.plaintext)

        outp.close()

    def load_ciphertext(self):
        """
        load_ciphertext()           Load Ciphertext of note to file named self.filename
        :return:
        """
        # TODO add exception handling
        with open(get_note_fullpath(self.filename), "r") as outp:
            self.ciphertext = outp.read()
            self.plaintext = ''

        outp.close()

    def load_plaintext(self):
        """
        load_plaintext()           Load plaintext of note to file named self.filename
        :return:
        """
        # TODO add exception handling
        with open(get_note_fullpath(self.title), "r") as outp:
            self.plaintext = outp.read()
            self.ciphertext = ''

        outp.close()

    def load_note(self, filename):
        """
        load_note()         loads a note from a file assigning to plaintext or
                            ciphertext depending on file extension
                            note 'filename' should exist in

        :param filename:    fullpath of filename
        (nb. class init(filename="xxx" will call import_note with the full path of xxx inside the USE'd notebook)

        :return bool:       returns success or failure
        """
        if not os.path.exists(get_note_fullpath(filename)):
            return False

        _title, _ext = os.path.splitext(self.filename)

        if _ext == GPGEXT:
            self.load_ciphertext()
        else:
            self.load_plaintext()

        return True

    # TODO rewrite using GPG encryption

    def encrypt(self):
        """encrypt Plaintext to Ciphertext"""
        # dummy encryption
        self.ciphertext = "%% " + self.plaintext
        self.plaintext = ""
        self.filename = self.filename + '.asc'

    def decrypt(self):
        """encrypt Plaintext to Ciphertext"""
        self.plaintext = self.ciphertext[3:]
        self.ciphertext = ""


if __name__ == "__main__":
    pass

