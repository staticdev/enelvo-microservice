# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from enelvo.normaliser import Normaliser

def create_app(test_config=None):
    norm = Normaliser(tokenizer='readable')

    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False # retrieve UTF-8 messages

    @app.route('/reply', methods=['POST'])
    def reply():
        """Fetch a reply from RiveScript.
        Parameters (JSON):
        * username
        * message
        * vars
        """
        params = request.json
        if not params:
            return jsonify({
                "status": "error",
                "error": "Request must be of the application/json type!",
            })

        message  = params.get("message")
        
        # Make sure the required params are present.
        if message is None:
            return jsonify({
                "status": "error",
                "error": "message is a required key",
        })
        
        try:
            # Get a reply from the Normaliser.
            reply = norm.normalise(message)
        except AttributeError as e:
            return jsonify({
                "status": "error",
                "error": "exception thrown: " + str(e),
            })
        
        # Send the response.
        return jsonify({
            "status": "ok",
            "reply": reply
        })

    return app