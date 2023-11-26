from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.uic import loadUi
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager
from helpers.shared_helpers.file_management.file_storage_manager import file_storage_manager


class ui_menu_item(QWidget):

    def __init__(
            self, 
            menu_item_name,
            menu_item_id, 
            parent=None,
            ui_manager = None
        ):

        super().__init__(parent)

        self.menu_item_name = menu_item_name
        self.menu_item_id = menu_item_id
        # this will hold some shared definitions

        self.ui_manager = ui_manager
        # this will set a reference to the UI manager

        self.global_params: global_paramenters = global_paramenters()
        self.logger:log_manager = log_manager()
        # this will set the global references

        relative_path_of_ui_file = "ui\components\menu_item\menu_item.ui"
        resource_manager:file_storage_manager = file_storage_manager(
            self.global_params
        )
        absolute_path_of_item = resource_manager.resource_path(relative_path_of_ui_file)

        loadUi(absolute_path_of_item, self)
        # the above code is used to load the UI

        self.implement_text_label()



    # ----------------------------
    # SETUP FUNCTIONS
    # ---------------------------
    # this will add setup functions that 
    # will be used to create the respective
    # menu items


    # this will set the text label
    def implement_text_label(
        self
    ):
        self.main_label.setText(self.menu_item_name)
        # this will set the welcome message


