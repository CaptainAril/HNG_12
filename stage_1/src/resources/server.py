from flask import jsonify, request
from flask_restful import Resource

from src.utilities.number_manager import NumManager


class ServerResource(Resource):

    @staticmethod
    def status():
        return jsonify({'status': 'OK'}), 200
    

    @staticmethod
    def number():
        number = request.args.get('number', None)
        if number:
            try:
                number = int(number)
                number = abs(number)

                num = NumManager(number)

                return jsonify(
                    {
                        "number": number,
                        "is_prime": num.is_prime,
                        "is_perfect": num.is_perfect,
                        "properties": num.properties,
                        "digit_sum": num.digit_sum,
                        "fun_fact": num.fun_fact
                    }
                ), 200
            
            except ValueError:
                return jsonify({"number": number, 'error': True}), 400
        return jsonify({"number": "no number provided", 'error': True}), 400