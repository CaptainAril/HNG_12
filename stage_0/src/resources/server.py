from datetime import datetime, timezone

from flask.json import jsonify
from flask_restful import Resource

from .. import config


class ServerResource(Resource):

    @staticmethod
    def status():
        return jsonify({"status": "ok"}), 200
    

    @staticmethod
    def basic_info():
        return jsonify({
            "email": config.slack_email,
            "current_datetime": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "github_url": config.github_repo_url
            }), 200