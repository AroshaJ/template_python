from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager

from helpers.shared_helpers.file_management.file_storage_manager import file_storage_manager
from helpers.sign_in.sign_in_manager import sign_in_manager



# the main_interface is called after the user successfully 
# signs in. It will allow the user to actually 
# access the menu and all application functions. From this point
# all application functions exist within a stacked widget that sits 
# underneath the respective main_interface. Clicking on menu items
# will change these items in and out as required. 
class main_interface(QMainWindow):

    def __init__(
        self,
        ui_manager
    ):
        super(main_interface, self).__init__()

        self.ui_manager = ui_manager
        # this will set a reference to the UI manager

        self.global_params: global_paramenters = global_paramenters()
        self.logger:log_manager = log_manager()
        # this will set the global references

        relative_path_of_ui_file = "ui\components\main_interface\main_interface.ui"
        resource_manager:file_storage_manager = file_storage_manager(
            self.global_params
        )
        absolute_path_of_item = resource_manager.resource_path(relative_path_of_ui_file)

        loadUi(absolute_path_of_item, self)
        # the above code is used to load the UI

        self.implement_interactions()
        # this will set up the required interactions and any initialisation items

        self.logger.log_information('main interface initialised')


    # this function will implement any interactions 
    # with our interface to generate the relevant 
    # functions
    def implement_interactions(self):
        pass


    # this will set the core labels in the application
    def implement_labels(
        self,
        current_user,
        application_version
    ):
        user_string = "Welcome " + current_user
        self.header_label.setText(user_string)
        # this will set the welcome message

        self.application_version.setText(application_version)
        # this will set the application version
