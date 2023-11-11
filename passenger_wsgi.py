import sys
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
   load_dotenv(dotenv_path)

USER = os.environ.get('REG_RU_ID')
NAME = os.environ.get('HOST_VENV_NAME')

INTERP = os.path.expanduser("/var/www/" + USER + "/data/" + NAME + "/bin/python")
print(INTERP)
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from bot import application