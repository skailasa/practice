"""
Simple App
"""
from flask import Flask, request, jsonify

from alchemist import Laboratory


app = Flask('alchemist')

@app.route('/', methods=['GET', 'POST'])
def ping():
    shelves = request.json
    lab = Laboratory(shelves)
    result = lab.run_experiment()
    return jsonify(result)


def run():
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    run()
