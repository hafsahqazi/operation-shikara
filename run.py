from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    dictionary = {
        'Hafsah': 'Stupid',
        'Musab': 'Genius'
    }
    return jsonify(dictionary)


app.run(host="0.0.0.0", use_reloader=False)
