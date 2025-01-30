""" 
server.py

Route for server
"""

from flask import Blueprint

from ..resources import ServerResource

ServerBlueprint = Blueprint("task", __name__)

ServerBlueprint.route("/api/status", methods=["GET"])(ServerResource.status)
ServerBlueprint.route("/api/basic-info", methods=["GET"])(ServerResource.basic_info)

