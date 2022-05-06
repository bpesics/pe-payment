from flask import Flask, request
import random
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/health")
def health():
    return "ok"

@app.route("/api/v1/charge", methods=['POST'])
def charge():
    content_type = request.headers.get('Content-Type')
    results_list = ['true', 'false']

    if (content_type == 'application/json'):
        app.logger.info('json request => ' + str(request.json))
        return {"result": random.choice(results_list)}
    else:
        return 'Content-Type not supported!'