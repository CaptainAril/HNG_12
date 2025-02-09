""" 
server.py

Route for server
"""


from flask import Blueprint

from ..resources import ServerResource

ServerBlueprint = Blueprint("task", __name__)

ServerBlueprint.route("/status", methods=["GET"])(ServerResource.status)
ServerBlueprint.route("/classify-number", methods=["GET"])(ServerResource.number)