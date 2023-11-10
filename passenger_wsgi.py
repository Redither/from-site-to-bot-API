import sys

import os

USER = os.environ.get('REG_RU_ID')
NAME = os.environ.get('HOST_VENV_NAME')

INTERP = os.path.expanduser("/var/www/" + USER + "/data/" + NAME + "/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from bot import application