# coding=utf-8

from backend.extensions import db


association_draw_groups_players = db.Table(
    'association_draw_groups_players', db.Model.metadata,
    db.Column('player_id', db.Integer, db.ForeignKey('players.id')),
    db.Column('draw_group_id', db.Integer, db.ForeignKey('draw_groups.id')),
)


class DrawGroup(db.Model):
    __tablename__ = 'draw_groups'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    game = db.relationship("Game", back_populates='draw_groups')
    players = db.relationship('Player', secondary=association_draw_groups_players, back_populates='draw_groups')

    def __init__(self, game):
        self.game = game
