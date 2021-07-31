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
    :return none:
    """
    # write config to config file
    with open(get_config_file(), "w") as configf:
        toml.dump(conf, configf)

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

"""
def get_default_notebook(self):
    return self.config.defaultnotebook

def get_use_notebook(self):
    return self.config.usenotebook

def get_default_notebook_fullpath(self):
    return self.default_fullpath

def get_use_notebook_fullpath(self):
    return self.use_fullpath

def get_notebooks(self):
    # Return a collection of all existing notebooks
    return [
        d
        for d in os.listdir(self.config.notesdir)
        if os.path.isdir(os.path.join(self.config.notesdir, d))
    ]

def get_notes(self, notebook):
    #Return a collection of all notes within a specified notebook
    return os.listdir(notebook.fullpath)

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

def prepend_use_notebook(self, title):
    #prepend fullpath of file
 
    return f"{self.config.notesdir}/{self.config.usenotebook}/{title}"

def prepend_a_notebook(self, notebook, title):
    #prepend fullpath of file

    return f"{self.config.notesdir}/{notebook}/{title}"

"""

# ============== encryption functions ====================#


# TODO rewrite using GPG encryption
def encrypt(plaintext):
    """encrypt Plaintext to Ciphertext"""
    # dummy encryption
    ciphertext = "%% " + plaintext
    plaintext = ""
    return ciphertext

def decrypt(ciphertext):
    """encrypt Plaintext to Ciphertext"""
    plaintext = ciphertext[3:]
    ciphertext = ""
    return plaintext



# ================ notebook functions ==================#

def create_notebook(title):
    notebookname = title.replace(" ", "_")
    notebookpath = self.config.notesdir + "/" + self.notebookname

    if not os.path.exists(self.notebookpath):
        os.mkdir(self.notebookpath, mode=0o700)

    return os.path.exists(self.notebookpath)

def rename_notebook(oldtitle, newtitle):
    """rename a notebook
    Renames existing notebook as title
    """
    title = title.replace(" ", "_")
    frompath = self.notebookpath
    topath = self.config.notesdir + "/" + title

    if os.path.exists(self.notebookpath):
        os.rename(frompath, topath)
        self.notebookpath = topath

    return os.path.exists(self.notebookpath)

def duplicate_notebook(oldtitle, newtitle):
    """duplicate a notebook"""
    title = title.replace(" ", "_")
    frompath = self.notebookpath
    topath = self.config.notesdir + "/" + title

    if os.path.exists(frompath) and not os.path.exists(topath):
        shutil.copytree(frompath, topath)
    return os.path.exists(topath)

def delete_notebook(title):
    """delete notebook and notes"""
    if os.path.exists(self.notebookpath):
        shutil.rmtree(self.notebookpath)
    return not os.path.exists(self.notebookpath)

def use_notebook(config, title):
    """use notebook"""
    title = title.replace(" ", "_")
    n = self.config.notesdir + "/" + title
    if os.path.exists(self.config.notesdir + "/" + title):
        self.notebookname = title
        self.notebookpath = self.config.notesdir + "/" + self.notebookname
        self.config.usenotebook = title
    return

def set_default_notebook(config, title):
    """switch back to default notebook"""
    self.config.usenotebook = self.config.defaultnotebook



# ==================================#


class Notes:
    """
    Notes class for handling notes objects
    """

    def __init__(self):
        self.config = Config()
        self.config.read_config()
        self.testinit = True
        self.plaintext = ""
        self.ciphertext = ""
        self.notebook = ""
        self.notetitle = ""
        self.notefullpath = ""

    def create(self, title):
        """add a note"""
        title = title.replace(" ", "_")
        titlepath = self.prepend_use_notebook(title)

        if os.path.exists(titlepath):
            return False

        self.notetitle = title
        self.notefullpath = titlepath

        #        with open(self.notefullpath, 'w') as nf:
        #            nf.write('')    # touch notefile
        #            nf.close()

        return self

    def open(self, filename):
        """add a note"""
        titlepath = self.prepend_use_notebook(filename)

        ftitle, fext = os.path.splitext(filename)

        if not os.path.exists(titlepath):
            return False

        self.notetitle = ftitle
        self.notefullpath = titlepath

        with open(self.notefullpath, "r") as nf:
            textcontent = nf.read()
            nf.close()

        if fext == ".asc":
            self.ciphertext = textcontent
            self.plaintext = ""
        else:
            self.ciphertext = ""
            self.plaintext = textcontent

    def set_plaintext(self, pt):
        """Save PT parameter to object"""
        self.plaintext = pt

    def set_ciphertext(self, ct):
        """Save CT parameter to object"""
        self.ciphertext = ct

    def save_ciphertext(self):
        """Save CT to file"""
        with open(self.prepend_use_notebook(self.notetitle + ".asc"), "w") as outp:
            outp.write(self.ciphertext)

    def save_plaintext(self):
        """Save PT to file"""
        with open(self.prepend_use_notebook(self.notetitle), "w") as outp:
            outp.write(self.plaintext)

    def import_note(self, filename):
        """import a note from a file"""
        if not os.path.exists(filename):
            return False

        with open(filename, "r") as imp:
            self.plaintext = imp.read()
            self.notetitle = filename.replace(" ", "_")
            self.notefullpath = self.prepend_use_notebook(filename)

            imp.close()

    def rename(self, newname):
        """rename a note"""
        newname = self.prepend_use_notebook(newname.replace(" ", "_"))

        if not os.path.exists(self.prepend_use_notebook(self.notetitle)):
            return False

        shutil.move(self.prepend_use_notebook(self.notetitle), newname)

        return os.path.exists(newname)

    def duplicate(self, newname):
        """duplicate a note"""
        newname = self.prepend_use_notebook(newname.replace(" ", "_"))

        if not os.path.exists(self.prepend_use_notebook(self.notetitle)):
            return False

        shutil.copy2(self.prepend_use_notebook(self.notetitle), newname)

        return os.path.exists(newname)

    def delete(self):
        """delete note"""
        # TODO write method
        #        title = title.replace(" ","_")
        pass

    def copy_to(self, notebook):
        """copy a note to another notebook"""
        newname = self.prepend_a_notebook(notebook, self.notetitle)
        if os.path.exists(newname):
            return False

        shutil.copy2(self.prepend_use_notebook(self.notetitle), newname)

        return os.path.exists(newname)

    def move_to(self, notebook):
        """move a note to new notebook"""
        newname = self.prepend_a_notebook(notebook, self.notetitle)

        if not os.path.exists(self.prepend_use_notebook(self.notetitle)):
            return False

        shutil.move(self.prepend_use_notebook(self.notetitle), newname)

        return os.path.exists(newname)

    def encrypt(self):
        """encrypt Plaintext to Ciphertext"""
        # dummy encryption
        self.ciphertext = "%% " + self.plaintext
        self.plaintext = ""

    def decrypt(self):
        """encrypt Plaintext to Ciphertext"""
        self.plaintext = self.ciphertext[3:]
        self.ciphertext = ""

    #    def save(self):
    #        """save note"""
    #        pass
    #
    #    def saveAs(self, filename):
    #        """save as note with new filename"""
    #        pass
    #
    #    def view(self):
    #        """view note"""
    #        pass
    #
    #    def edit(self):
    #        """edit note"""
    #        pass



if __name__ == "__main__":

    print(f"_default_config = {_default_config}")

    pass
