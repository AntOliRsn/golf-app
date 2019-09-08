# coding=utf-8

from backend.extensions import db
from backend.draw_group.classes import association_draw_groups_players


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    levels = db.relationship("Level", back_populates="player")
    draw_groups = db.relationship('DrawGroup', secondary=association_draw_groups_players, back_populates='players')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Level(db.Model):
    __tablename__ = "levels"

    id = db.Column(db.Integer, primary_key=True)
    date_valid = db.Column(db.Date)
    level = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player = db.relationship('Player', back_populates='levels')

    def __init__(self, player, date_valid, level):
        self.player = player
        self.date_valid = date_valid
        self.level = level
