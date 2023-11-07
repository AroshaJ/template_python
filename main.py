from datetime import datetime
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager
from helpers.shared_helpers.file_management.file_storage_manager import file_storage_manager


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

    logger.log_information('info logging test')
    logger.log_error_message('error test')

    try:
        # Some operation that may raise an exception
        result = 10 / 0
    except Exception as e:
        logger.log_exception(e)  # Pass the exception to the logging function


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











# this is used to invoke the main method. 
if __name__ == "__main__":
    main()

