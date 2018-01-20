# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from enelvo.normaliser import Normaliser

NORM = Normaliser()

APP = Flask(__name__)
APP.config['JSON_AS_ASCII'] = False # retrieve UTF-8 messages

@APP.route('/reply', methods=['POST'])
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
    
    # Get a reply from the Normaliser.
    reply = NORM.normalise(message)
    
    # Send the response.
    return jsonify({
        "status": "ok",
        "reply": reply
    })
