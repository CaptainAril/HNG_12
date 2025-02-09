import json
from collections import OrderedDict

from flask import Response, jsonify, request
from flask_restful import Resource

from src.utilities.number_manager import NumManager


class ServerResource(Resource):

    @staticmethod
    def status():
        return jsonify({'status': 'OK'}), 200
    

    @staticmethod
    def number():
        number = request.args.get('number', '')
        
        try:
            if number:
                number = int(number)

                num = NumManager(number)

                response_data = OrderedDict(
                    [
                        ("number", number),
                        ("is_prime", num.is_prime),
                        ("is_perfect", num.is_perfect),
                        ("properties", num.properties),
                        ("digit_sum", num.digit_sum),
                        ("fun_fact", num.fun_fact)
                    ]
                )

                # return jsonify(response_data), 200
                response_json = json.dumps(response_data, indent=4)
                return Response(response_json, mimetype='application/json', status=200)
            
        except Exception as e:
            print(e)
            return jsonify({"number": number, 'error': True}), 400
        return jsonify({"number": number, 'error': True}), 400