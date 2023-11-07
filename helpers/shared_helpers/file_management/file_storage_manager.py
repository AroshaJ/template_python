from helpers.global_references.global_parameters import global_paramenters
import os
from ctypes import windll, wintypes, byref
from pathlib import Path
import sys
import shutil

class file_storage_manager():

    def __init__(
        self,
        global_params: global_paramenters
    ):

        self.global_params = global_params
        # this will set the global reference



    # ------------------------
    # SHARED FUNCTIONS
    # ------------------------
    # the following are shared
    # functions across the 
    # respective dependent functions

    # this will return the correct path when using pyinstaller
    def resource_path(
        self,
        relative_path
    ):

        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        
        return os.path.join(base_path, relative_path)
        # this will return the absolute path

    def get_current_documents_folder(
        self
    ):
        if os.name == 'nt':
            # this is for windows 
            documents_path = Path(os.environ.get("USERPROFILE", ""), 'Documents')
            # Alternatively, you could use ctypes to get the folder location more robustly
            # but for simplicity, we're using the USERPROFILE environment variable here.
        else:
            # On Unix and macOS, it's typically under the user's home directory
            documents_path = Path.home() / 'Documents'

        return documents_path
    
    # this will create a base folder
    # if it doesn't already exist. Please
    # note that the base folder is named
    # after the app using the app name
    def initialise_base_folder(
        self
    ):
        app_name = self.global_params.application_name
        # this is the application name

        app_name_camel_case = self.to_camel_case(app_name)
        # this will convert the name to camel case

        full_path = self.global_params.documents_folder_path + app_name_camel_case
        # this will generate the full path

        self.create_folder_if_doesnt_exist(full_path)
        # this will create the folder

        self.global_params.root_folder_path = full_path
        # this will set the root folder


    # this will create the respective folder if
    # it doesn't exist
    def create_folder_if_doesnt_exist(
        self,
        folder_path
    ):
        exists = self.does_folder_exist(
            folder_path
        )

        if exists == False:
            self.create_folder_in_path(folder_path)

    


    # ---------------------
    # SUPPORT FUNCTIONS
    # ---------------------
    # this will set up the 
    # required support functions

    def to_camel_case(
        self,
        full_string
    ):
        words = full_string.split()
        # Capitalize the first letter of each word except the first one
        # and join them together.

        return_value = words[0].lower() + ''.join(word.capitalize() for word in words[1:])

        return return_value
    
    # this will return true if 
    # the respective folder exists
    def does_folder_exist(
        self,
        folder_path
    ):
        folder = Path(folder_path)
        if not folder.is_dir():
            return False
        else:
            return True
        
    # this will create the given 
    # folder at the respective 
    # location
    def create_folder_in_path(
        self,
        folder_path
    ):
        folder = Path(folder_path)
        folder.mkdir(parents=True, exist_ok=True)
