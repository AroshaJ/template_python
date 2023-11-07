import logging
import logging.handlers
import os


# this will handle all logging events that need
# to run when setting up a given logging function
class log_manager(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(log_manager, cls).__new__(cls)
            print('initialising log manager class')
        return cls.instance
    
    def __init__(self):

        self.logger = logging.getLogger('MyAppLogger')
        # this will create a central logger

        self.configure_logger()
        # this will create the logger


    
    # set up the initial configuration
    def configure_logger(
        self
    ):
        self.logger.setLevel(logging.DEBUG)  # Capture all levels of logging

        # Define log file name pattern
        log_filename = 'app_log.log'

        # Use RotatingFileHandler to split the log into multiple files
        handler = logging.handlers.RotatingFileHandler(
            log_filename, maxBytes=2*1024*1024, backupCount=10, mode='a'
        )

        # Define the formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - [%(module)s: %(funcName)s]: %(message)s'
        )
        handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(handler)

    
    # ------------------------
    # SHARED FUNCTIONS
    # -----------------------
    # the following are shared 
    # functions used across the
    # application

    # this is used to log an exception and should log a full error stack trace
    def log_exception(
        self,
        exception: Exception
    ):  
        self.logger.error(
            "An exception occurred", 
            exc_info=True,
            stacklevel=2
        ) 

    # this will log a dedicated error message
    def log_error_message(
        self,
        error_message
    ):
        self.logger.error(
            f"An exception occurred: {error_message}",
            stacklevel=2
        )

    # log a generic informational 
    # message
    def log_information(
        self,
        message_to_log
    ):  
        
        self.logger.info(
            message_to_log,
            stacklevel=2
        )  

    # a warning message
    def log_warning(
        self,
        warning_message
    ):  
        
        self.logger.warning(
            warning_message,
            stacklevel=2
        )  

