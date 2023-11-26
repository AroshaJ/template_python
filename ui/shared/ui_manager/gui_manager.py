
import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import Qt
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager
from helpers.shared_helpers.chatgpt_management.chatgpt_manager import chatgpt_manager
from helpers.shared_helpers.file_management.file_storage_manager import file_storage_manager
from ui.components.login_page.login_page import login_page
from ui.components.main_interface.main_interface import main_interface
from ui.components.menu_item.ui_menu_item import ui_menu_item


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

            # REFERENCE VARIABLES
            self.menu_items = [] # this will hold the menu items


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

    

    # ----------------------------
    # INTERFACE INITIALISATION
    # ---------------------------
    # this will set up the initial 
    # configuration for the respective
    # interfaces


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
    
    def initialise_main_interface(
        self
    ):
        self.logger.log_information('started initialising main window')
        # this will set up the initialisation of the 
        # main window

        self.main_interface_window = main_interface(self)

        self.initialise_main_menu_items()
        # this will create the menu items

        self.main_interface_window.show()

        current_user = self.global_params.currently_logged_in_user
        current_user_name = current_user[0]
        # this will get the current user details

        version_num = self.global_params.version_number
        version_date = self.global_params.release_date
        version_string = 'Version ' + version_num + ' ' + version_date

        self.main_interface_window.implement_labels(current_user_name, version_string)
        # this will set the key labels

        # this will set up the stacked widgets
        # self.initialise_widgets_in_main_interface()

        # this will set the required references
        # self.set_initial_configurations_for_widgets()

        # this will open the dashboard widget
        # self.initialise_landing_section()


    def initialise_main_menu_items(
        self
    ):
        self.add_main_menu_item(
            'item 1',
            'item_1'
        )

        self.add_main_menu_item(
            'item 2',
            'item_2'
        )

        # position menu items
        i = 0
        x_position = 22
        base_y_pos = 59
        y_increment = 48 # each new item increments by this many pixels

        for _menu in self.menu_items:
            _item:ui_menu_item = _menu

            y_pos = base_y_pos + (y_increment * i)
            _item.move(x_position, y_pos)

            i = i + 1
            # this will increment the item


    # ----------------------------
    # INTERFACE CONTROLE
    # ---------------------------
    # this will control the respective
    # interface based in flight 
    # config changes


    # this will show/hide
    # the sign in window. It expects a boolean as
    # input
    def show_sign_in_interface(
        self,
        show
    ):
        if show == False:
            self.sign_in_window.hide()
        else:
            self.sign_in_window.show()



    # ----------------------------
    # SHARED CONFIG FUNCTIONS
    # ---------------------------
    # this will add shared configuration
    # functions

    # this will create a new menu item
    def add_main_menu_item(
        self,
        menu_item_name,
        menu_item_id
    ):
        for _menu in self.menu_items:
            _item:ui_menu_item = _menu
            _id = _item.menu_item_id

            if _id == menu_item_id:
                return None
            # this will prevent creation of a 
            # new menu item as it already exists
        
        _newItem: ui_menu_item = ui_menu_item(
            menu_item_name,
            menu_item_id,
            parent=self.main_interface_window.menu_container,
            ui_manager= self
        )
        # this will create the new item

        self.menu_items.append(_newItem)
        # this will add the item to the register


