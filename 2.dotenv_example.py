# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.demo_env')  #Path to the file
load_dotenv(dotenv_path)

DOMAIN = os.environ["DOMAIN"]
ROOT_URL = os.environ.get("ROOT_URL")
print(DOMAIN)
print(ROOT_URL)
os.environ["DOMAIN"]="hello"
print(os.environ["DOMAIN"])
