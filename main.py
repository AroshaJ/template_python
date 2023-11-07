from datetime import datetime
from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager


def main():
    # this will define the respective main function

    start = datetime.now()
    start_time = start.strftime("%H:%M:%S")
    print("Start Time =", start_time)

    # INITIALISE SEQUENCE
    print('initialised app')

    # initialise the global parameters
    logger = log_manager()
    global_param = global_paramenters()

    logger.log_information('info logging test')
    logger.log_error_message('error test')

    try:
        # Some operation that may raise an exception
        result = 10 / 0
    except Exception as e:
        logger.log_exception(e)  # Pass the exception to the logging function










# this is used to invoke the main method. 
if __name__ == "__main__":
    main()

