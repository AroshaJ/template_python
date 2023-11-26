


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


    # -------------------------------
    # RELEASE MANAGEMENT
    # -------------------------------
    # The following covers any  
    # relevant release management items

    version_number = '0.0.0.1' 
    release_date = '10 Oct 2023'


    # -------------------------------
    # SIGN IN CONFIGURATIONS
    # -------------------------------
    # The following captures the core 
    # confurations related to sign ins

    max_sign_in_attempts_allowed = 3

    currently_logged_in_user = None
    # this will hold the details for the currently logged in user

    # USER INFORMATION
    # Log in information for this application is hard-coded. New deployments are required
    # In order to manage the respective information related to the application  
    # the array of users contains each user entry which holds the following information
    # First Name, Last Name, UserName, Password
    registered_users = [
        ["Rosh","Jayawardena","AroshaJ","Snaddy42"],
        ["Nirmal","Jayawardena","NirmalJ","Snaddy42"]
    ]



    # -------------------------------
    # CHAT GPT CONFIGURATIONS
    # -------------------------------
    # The following captures the core 
    # confurations related to chat gpt
    chat_gpt_key_name = 'python_projects'
    chat_gpt_app_key = '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'

