# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

from .entity import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    golf = Column(String)
    game_format = Column(String)
    game_date = Column(Date)
    game_details = relationship("GameDetails", back_populates="game", uselist=False)
    draw_groups = relationship("DrawGroup", back_populates="game")

    def __init__(self, golf, game_format, game_date):
        self.golf = golf
        self.game_format = game_format
        self.game_date = game_date


class GameDetails(Base):
    __tablename__ = "games_details"

    id = Column(Integer, primary_key=True)
    max_hcp_man = Column(Integer)
    max_hcp_woman = Column(Integer)
    tee_off = Column(Time)
    fee = Column(Integer)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game", back_populates="game_details", uselist=False)

    def __init__(self, game, max_hcp_man=None, max_hcp_woman=None, tee_off=None, fee=None):
        self.game = game
        self.max_hcp_man = max_hcp_man
        self.max_hcp_woman = max_hcp_woman
        self.tee_off = tee_off
        self.fee = fee
