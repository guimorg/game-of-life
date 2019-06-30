import numpy as np

from flask import (
    Flask,
    request,
    jsonify,
    render_template
)

from game.life import Game


app = Flask(
    __name__
)

game = Game()


@app.route('/api/')
def index_api():
    """
        This is basically a Healthcheck endpoint.
    """
    return jsonify({'app': 'healthy'})


@app.route('/api/', methods=['POST'])
def process():
    """
        This functions process the array obtained by the frontend.
        It is independent of previous states, it takes current generation,
        calls life.next_generation and returns an array.
    """
    current_gen = request.get_json()  # Must convert JSON to Numpy Array
    # Life
    next_generation = game.next_generation(current_gen)
    return jsonify(next_generation)  # Maybe need to convert Numpy Array to JSON


@app.route('/')
def index():
    return 'Template rendered.'


if __name__ == "__main__":
    app.run()
