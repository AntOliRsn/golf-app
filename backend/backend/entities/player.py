# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from .entity import Base
from .draw_group import association_draw_groups_players


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    levels = relationship("Level", back_populates="player")
    draw_groups = relationship('DrawGroup', secondary=association_draw_groups_players, back_populates='players')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    date_valid = Column(Date)
    level = Column(Integer)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship('Player', back_populates='levels')

    def __init__(self, player, date_valid, level):
        self.player = player
        self.date_valid = date_valid
        self.level = level
