from flask import Flask, jsonify, request
from tunings import *

app = Flask(__name__)

@app.route('/')
def home():
    return "Tuning Api /guitar /bass /ukulele"

@app.route("/guitar", methods=["GET", "POST"])
def guitar():
    return jsonify({'Guitar Tunings': get_json('guitar', guitar_names, guitar_tunings)})

@app.route("/bass", methods=["GET", "POST"])
def bass():
    return jsonify({'Bass Tunings': get_json('bass', bass_names, bass_tunings)})

@app.route("/ukulele", methods=["GET", "POST"])
def ukulele():
    return jsonify({'Ukulele Tunings': get_json('ukulele', ukulele_names, ukulele_tunings)})


if __name__ == '__main__':
    app.run(debug=True)