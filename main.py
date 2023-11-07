from datetime import datetime
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager
from helpers.shared_helpers.file_management.file_storage_manager import file_storage_manager
from ui.shared.ui_manager.gui_manager import gui_manager
import ui.assets.resources


def main():
    # this will define the respective main function

    start = datetime.now()
    start_time = start.strftime("%H:%M:%S")
    print("Start Time =", start_time)

    # INITIALISE SEQUENCE
    print('initialised app')

    # initialise the global parameters
    global_param = global_paramenters()
    initialise_global_parameters(global_param)

    logger = log_manager()
    # this will set up the logger

    initialise_ui(
        global_param,
        logger
    )
    # this will set up the UI
    

# this will run the necessary initialisers
def initialise_global_parameters(
    global_param: global_paramenters
):
    storage_manager: file_storage_manager = file_storage_manager(global_param)
    # this will create the base item

    documents_folder = storage_manager.get_current_documents_folder()
    global_param.documents_folder_path = str(documents_folder) + "\\"
    # this will set the base documents path

    storage_manager.initialise_base_folder()
    # this will set up the base folder


def initialise_ui(
    global_param: global_paramenters,
    logger: log_manager
):
    print('ui interface initialised')

    ui_manager: gui_manager = gui_manager()
    # this will set up the ui manager

    ui_manager.initialise_sign_in_interface()
    # this will set up the sign in process












# this is used to invoke the main method. 
if __name__ == "__main__":
    main()

