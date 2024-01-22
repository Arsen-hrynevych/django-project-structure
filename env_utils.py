import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / '.env'

# Load the environment variables from the .env file
load_dotenv(env_path)


# Function to get environment variables with a default value
def get_env_variable(variable_name):
    return os.environ.get(variable_name)


# Define your environment variables

# Other Django Settings
DJANGO_SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

# Project state
PROJECT_STATE = get_env_variable('PROJECT_STATE')