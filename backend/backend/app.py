# coding=utf-8

from flask import Flask

# Import extensions
from backend.extensions import cors, db, ma

# Import submodules
from backend.player.classes import Player, Level
from backend.game.classes import Game, GameDetails
from backend.draw_group.classes import DrawGroup


def create_app():

    app = Flask(__name__)
    app.config.from_object("backend.config.cfg")
    register_extensions(app)

    return app


def register_extensions(app):

    cors.init_app(app)
    db.init_app(app)
    ma.init_app(app)


if __name__ == "__main__":

    from datetime import datetime, time
    from backend.player.schemas import player_schema, level_schema
    from backend.game.schemas import game_schema, game_details_schema
    from backend.draw_group.schemas import draw_group_schema


    app = create_app()

    with app.app_context():

        db.create_all()

        players = db.session.query(Player).all()
        player_1 = players[0]
        level_1 = player_1.levels[0]
        result = player_schema.dump(player_1)
        print(result)

        result = level_schema.dump(level_1)
        print(result)


        player_1 = Player("Antoine", "Rosin")
        player_2 = Player("Guillaume", "Rosin")
        player_3 = Player("Jon", "Rosin")


        level_1_1 = Level(player_1, datetime(2019,7,1), 15)
        level_1_2 = Level(player_1, datetime(2019,8,1), 19)
        level_2_1 = Level(player_2, datetime(2019,8,1), 23)

        player_1.levels
        player_2.levels

        game_1 = Game("tamarin", "not_known", datetime(2019,9, 10))
        game_details_1 = GameDetails(game_1, max_hcp_man=13, tee_off=time(11,30), fee=200)

        draw_group_1 = DrawGroup(game_1)
        draw_group_2 = DrawGroup(game_1)

        draw_group_1.players = [player_1, player_2]
        draw_group_2.players = [player_3]

        game_1.draw_groups


        db.session.add(player_1)
        db.session.add(player_2)

        db.session.add(level_1_1)
        db.session.add(level_1_2)
        db.session.add(level_2_1)

        db.session.add(game_1)
        db.session.add(game_details_1)
        db.session.add(draw_group_1)
        db.session.add(draw_group_2)

        db.session.commit()
        db.session.close()