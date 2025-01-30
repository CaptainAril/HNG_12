""" 
wsgi.py

web server gateway
Application entry point in production
"""

from . import config
from .server import server as app

if __name__ == "__main__":
    if config.env == 'prod':
        app.run()
