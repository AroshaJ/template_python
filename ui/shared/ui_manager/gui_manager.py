
import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import Qt
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager
from ui.components.login_page.login_page import login_page


class gui_manager(object):

    _is_initialized = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(gui_manager, cls).__new__(cls)
        return cls.instance
    

    def __init__(self):

        if self._is_initialized == False:

            self.global_params: global_paramenters = global_paramenters()
            self.logger:log_manager = log_manager()
            # global references

            # INTERFACE VARIABLES
            sign_in_window = None
            main_interface_window = None


            self.initial_configuration()

            self._is_initialized = True
            # this will ensure that we don't run the 
            # initialiser again


    # ----------------------------
    # INITIAL CONFIGURATION
    # ---------------------------
    # this will set up the initial 
    # configuration for the respective
    # class

    def initial_configuration(
        self
    ):
        self.logger.log_information(
            'GUI Manager initialised'
        )


    # set up the sign in interface
    def initialise_sign_in_interface(
        self
    ):
        app = QApplication(sys.argv)
        self.sign_in_window: login_page = login_page(
            self
        )
        self.sign_in_window.show()
        app.exec()