from flask import Blueprint, jsonify
from backend.player.classes import Player
from backend.player.schemas import players_schema, player_schema, level_schema

player_blueprint = Blueprint("player", __name__)

@player_blueprint.route("/players", methods=["GET"])
def get_players():
    """
    Get all Players.

    ---
    get:
     description: Get all Players
     summary: Get all Players
     tags:
       - Players
     responses:
       200:
         description: An array containing all of the Players
         content:
           application/json:
             schema:
               type: array
               items:
                 $ref: '#/definitions/Player'
    """
    all_players = Player.query.all()
    result = players_schema.dump(all_players)

    return jsonify(result)



