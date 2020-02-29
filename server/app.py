from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import numpy as np
import flask

import minesweeper

GAME = minesweeper.Game()

for row in GAME.mine_locations:
    print(row)

app = Flask(__name__, static_folder="../build")
CORS(app)


class NumpyEncoder(json.JSONEncoder):
    """
    Extends json dumps to recursively convert numpy arrays to lists
    """

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def format_game_state(game):
    """
    Returns json blob with current state of game

    Args:
        game (minesweeper.Game)

    Returns:
        response (string): json blog of game state
    """
    response = {
        "revealed_state": game.revealed_state,
        "unclicked_non_mine_count": game.unclicked_non_mine_count,
        "has_won": game.has_won,
        "has_lost": game.has_lost,
    }
    return json.dumps(response, cls=NumpyEncoder)


##
# API routes
##


@app.route("/ping", methods=["GET"])
def health_check():
    """ 
    Health check 
    """
    return "Response"


@app.route("/game_state", methods=["GET"])
def get_state():
    """ 
    Return current state 
    """
    return format_game_state(GAME)


@app.route("/click", methods=["POST"])
def make_click():
    """
    Click on cell and return updated game state
    """
    move_inputs = json.loads(flask.request.data)
    global GAME
    GAME.click(int(move_inputs["x"]), int(move_inputs["y"]))
    return format_game_state(GAME)


@app.route("/reset", methods=["POST"])
def reset_game():
    """
    Create new game with specified game parameters
    """
    game_inputs = json.loads(flask.request.data)
    global GAME
    GAME = minesweeper.Game(**game_inputs)
    return format_game_state(GAME)


##
# View route
##


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    """Return index.html for all non-api routes"""
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
