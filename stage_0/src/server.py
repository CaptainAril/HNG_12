"""
server.py

Application entry point
"""

from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS

from . import config, routes

server = Flask(__name__)
server.secret_key = config.secret_key

server.url_map.strict_slashes = False

with server.app_context():
    from .utilities import error_handlers

cors = CORS(
            server, 
            resources={r"/api/*": {"origins": "*"}},
            supports_credentials=True,
            max_age=3600
            )

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.app_root
        )

if __name__ == "__main__":
    server.debug = config.debug if config.env =='dev' else False
    if config.env == 'dev':
        server.run(host=config.app_host, port=config.app_port)