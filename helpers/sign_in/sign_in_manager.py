# this is used to manage the actual sign in of a given user
import os
import sys

from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager


class sign_in_manager():
    
    def __init__(self):
        
        self.global_params: global_paramenters = global_paramenters()
        self.logger:log_manager = log_manager()
        # this will set the global references

        self.invalid_attempts = 0
        self.max_attempts = self.global_params.max_sign_in_attempts_allowed
        # this will set up the required variables

    # -----------------------------
    # PROCESSING FUNCTIONS
    # ----------------------------
    # these are called directly

    # this will attempt to log in the user
    # it will return an array with a 
    # success status and a display message
    def log_in_user(
        self,
        username,
        password
    ):

        if self.invalid_attempts >= self.max_attempts:
            return_value = [False, "You are locked out"]
            self.logger.log_information("user locked out f{username}")

            return return_value
        # if max attempts have been reached

        clean_username = self.clean_credential_string(username)
        clean_password = self.clean_credential_string(password)
        # this will clean up the string

        valid_format = self.credentials_are_a_valid_format(clean_username, clean_password)
        # this will check if the credentials are of a valid format

        if valid_format == False:
            return_value = [False, "Invalid credentials, please try again"]
            self.invalid_attempts = self.invalid_attempts + 1

            self.logger.log_information("user entered invalid credentials f{username}")

            return return_value
        # this will end the function

        valid_user = self.do_credentials_belong_to_a_valid_user(clean_username, clean_password)
        # this will validate if these credentials belong to a user

        if valid_user == None:
            return_value = [False, "Invalid credentials, please try again"]
            self.invalid_attempts = self.invalid_attempts + 1

            self.logger.log_information("user entered invalid credentials f{username}")

            return return_value
        else:
            return_value = [True, "Welcome " + valid_user[0]]
            self.global_params.currently_logged_in_user = valid_user

            self.logger.log_information("user successfully logged in f{username}")

            return return_value

    # -----------------------------
    # SUPPORT FUNCTIONS
    # ----------------------------
    # these are called from dependent classes

    # this will check if the credentials are of a valid format
    def credentials_are_a_valid_format(
        self,
        clean_username,
        clean_password
    ):
        
        if clean_username == "":
            return False

        if clean_password == "":
            return False
        
        return True


    # this will check if the credentials belong to a valid user
    def do_credentials_belong_to_a_valid_user(
        self,
        clean_username,
        clean_password
    ):
        
        full_users = self.global_params.registered_users
        # this will get the full list

        for user in full_users:

            current_username = user[2]
            current_password = user[3]

            if (current_username == clean_username) & (current_password == clean_password):
                return user
                # this will end the loop and return the user

        # if the user is not found this will return none
        return None
        
    # this will clean up the input string. Essentially this 
    # just applies the trim function
    def clean_credential_string(
        self,
        string_to_clean
    ):
        return_value = string_to_clean.strip()
        return return_value