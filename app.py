# -*- coding: utf-8 -*-

""" Microservice for enelvo normalization method """

import flask
import enelvo.normaliser


def create_app():
    """ Application factory """
    norm = enelvo.normaliser.Normaliser(tokenizer='readable')

    app = flask.Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # retrieve UTF-8 messages

    @app.route('/reply', methods=['POST'])
    def reply():
        """Fetch a reply from RiveScript.
        Parameters (JSON):
        * username
        * message
        """
        params = flask.request.json
        if not params:
            return flask.jsonify({
                "status": "error",
                "error": "Request must be of the application/json type!",
            })

        message = params.get("message")

        # Make sure the required params are present.
        if message is None:
            return flask.jsonify({
                "status": "error",
                "error": "message is a required key",
            })

        try:
            # Get a reply from the Normaliser.
            reply = norm.normalise(message)
        except AttributeError as ex:
            return flask.jsonify({
                "status": "error",
                "error": "exception thrown: " + str(ex),
            })

        # Send the response.
        return flask.jsonify({
            "status": "ok",
            "reply": reply
        })

    return app
