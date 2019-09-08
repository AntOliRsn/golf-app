# coding=utf-8

from flask import Flask

# Import extensions
from .extensions import cors, db

# Import submodules
from .entities.entity import Base, Session, engine
from .entities.player import Player, Level
from .entities.game import Game, GameDetails
from .entities.draw_group import DrawGroup


def create_app():

    app = Flask(__name__)
    app.config.from_object("backend.config.cfg")
    register_extensions(app)


def register_extensions(app):

    cors.init_app(app)
    db.init_app(app)


if __name__ == "__main__":

    from datetime import datetime, time

    with app.app_context():

        db.create_all()

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

        session = Session()
        session.add(player_1)
        session.add(player_2)

        session.add(level_1_1)
        session.add(level_1_2)
        session.add(level_2_1)

        session.add(game_1)
        session.add(game_details_1)
        session.add(draw_group_1)
        session.add(draw_group_2)

        session.commit()
        session.close()