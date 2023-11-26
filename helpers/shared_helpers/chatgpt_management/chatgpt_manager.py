from helpers.global_references.global_parameters import global_paramenters
from helpers.logging.log_manager import log_manager
from openai import OpenAI

# this will set the required references
class chatgpt_manager():


    def __init__(self):
        
        self.global_params: global_paramenters = global_paramenters()
        self.logger:log_manager = log_manager()
        # global references

        self.client = None
        # this will hold the OpenAI client

        self.initial_configuration()
        # this will set the initial setup

    
    def initial_configuration(
        self
    ):
        app_key = self.global_params.chat_gpt_app_key
        self.client = OpenAI(
            api_key=app_key
        )



    # -----------------------
    # PUBLIC FUNCTIONS
    # ----------------------
    # this will apply the respective
    # public functions

    # this will be used to ask chat GPT a 
    # question with a prompt
    def ask_gpt(
        self,
        prompt
    ):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are providing answers in casual plain english."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return completion.choices[0].message