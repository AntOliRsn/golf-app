# coding=utf-8

from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from .entity import Base


association_draw_groups_players = Table(
    'association_draw_groups_players', Base.metadata,
    Column('player_id', Integer, ForeignKey('players.id')),
    Column('draw_group_id', Integer, ForeignKey('draw_groups.id')),
)


class DrawGroup(Base):
    __tablename__ = 'draw_groups'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game", back_populates='draw_groups')
    players = relationship('Player', secondary=association_draw_groups_players, back_populates='draw_groups')

    def __init__(self, game):
        self.game = game