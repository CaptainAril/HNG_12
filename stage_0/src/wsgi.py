""" 
wsgi.py

web server gateway
Application entry point in production
"""

from server import app

from . import config

if __name__ == "__main__":
    if config.env == 'prod':
        app.run()
