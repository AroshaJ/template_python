from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager

from helpers.shared_helpers.file_management.file_storage_manager import file_storage_manager
from helpers.sign_in.sign_in_manager import sign_in_manager



class login_page(QMainWindow):


    def __init__(
        self,
        ui_manager
    ):
        super(login_page, self).__init__()

        self.ui_manager = ui_manager
        # this will set a reference to the UI manager

        self.global_params: global_paramenters = global_paramenters()
        self.logger:log_manager = log_manager()
        self.sign_in_manager:sign_in_manager = sign_in_manager()
        # this will set the global references

        relative_path_of_ui_file = "ui\components\login_page\login_page.ui"
        resource_manager:file_storage_manager = file_storage_manager(
            self.global_params
        )
        absolute_path_of_item = resource_manager.resource_path(relative_path_of_ui_file)

        loadUi(absolute_path_of_item, self)
        # the above code is used to load the UI

        self.implement_interactions()
        # this will set up the required interactions

        self.logger.log_information('log in page initialised')

    
    # this function will implement any interactions 
    # with our interface to generate the relevant 
    # functions
    def implement_interactions(self):

        self.sign_in_button.clicked.connect(self.sign_in_function)
        # this will essentially apply a listener to the given button 
        # which is called sign_in_button

        self.password.returnPressed.connect(self.sign_in_function)
        # this will call the sign in function if the user hits enter from 
        # within the password field

        self.username.textChanged.connect(self.clear_error_message)
        self.password.textChanged.connect(self.clear_error_message)
        # this will clear any error message if the user selects the given fields. 


    #-------------------------
    # INTERACTIONS
    #-------------------------
    # the following cover off the interaction
    # functions

    # this is called when the user clicks the sign in button
    def sign_in_function(self):

        username_value = self.username.text()
        password_value = self.password.text()
        # this will get the required values

        self.logger.log_information('log in attempted for ' + username_value)

        sign_in_status = self.sign_in_manager.log_in_user(username_value, password_value)
        # this will sign in the user

        if sign_in_status[0] == False:
            message = sign_in_status[1]
            self.invalid_credentials.setText(message)
            # this will set the invalid message

        else:
            message = sign_in_status[1]
            self.open_main_interface_after_login()

    # this will clear any error messages
    def clear_error_message(self):
         
        self.invalid_credentials.setText("")
        # this will clear any messages

    # this will open the main interface after login
    def open_main_interface_after_login(
        self
    ):
        print('open main interface')
        
        self.ui_manager.initialise_main_interface()
        # this is done to initialise the respective main interface

        self.ui_manager.show_sign_in_interface(False)
        # this will hide the sign in interface















