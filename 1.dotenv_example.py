from dotenv import load_dotenv,dotenv_values

env_file=load_dotenv(".demo_env")  # take environment variables from .env.
data=dotenv_values(".demo_env")

print(data)




# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.