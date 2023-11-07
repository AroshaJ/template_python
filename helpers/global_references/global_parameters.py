


class global_paramenters(object):
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(global_paramenters, cls).__new__(cls)
            print('initialising global parameters class')
        return cls.instance
    

    # -------------------------------
    # CORE CONFIGURATIONS
    # -------------------------------
    # The following captures the core 
    # confurations that are required
    # in order to set up the respective
    # project. 

    application_name = 'Template Application'
    # this should be the full name of the application

    documents_folder_path = ''
    root_folder_path = ''
    # this will set the folder paths used across the board

