activate_this = '/var/www/wsgi/app3/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, "/var/www/wsgi/app3")

from app import app
application = app

