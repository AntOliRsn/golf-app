# coding=utf-8

from backend.extensions import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    golf = db.Column(db.String)
    game_format = db.Column(db.String)
    game_date = db.Column(db.Date)
    game_details = db.relationship("GameDetails", back_populates="game", uselist=False)
    draw_groups = db.relationship("DrawGroup", back_populates="game")

    def __init__(self, golf, game_format, game_date):
        self.golf = golf
        self.game_format = game_format
        self.game_date = game_date


class GameDetails(db.Model):
    __tablename__ = "games_details"

    id = db.Column(db.Integer, primary_key=True)
    max_hcp_man = db.Column(db.Integer)
    max_hcp_woman = db.Column(db.Integer)
    tee_off = db.Column(db.Time)
    fee = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    game = db.relationship("Game", back_populates="game_details", uselist=False)

    def __init__(self, game, max_hcp_man=None, max_hcp_woman=None, tee_off=None, fee=None):
        self.game = game
        self.max_hcp_man = max_hcp_man
        self.max_hcp_woman = max_hcp_woman
        self.tee_off = tee_off
        self.fee = fee
