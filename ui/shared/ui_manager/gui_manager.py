

from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager


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
