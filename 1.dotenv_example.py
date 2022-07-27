from dotenv import load_dotenv, dotenv_values

env_file = load_dotenv("env.txt")  # take environment variables from .env.
data = dotenv_values("env.txt")

print(data)

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
