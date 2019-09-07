# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from .entity import Base, Session, engine


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    levels = relationship("Level", back_populates="player")

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


if __name__ == "__main__":

    from datetime import datetime
    Base.metadata.create_all(engine)

    player_1 = Player("Antoine", "Rosin")
    player_2 = Player("Guillaume", "Rosin")

    level_1_1 = Level(datetime(2019,7,1), 15, player_1)
    level_1_2 = Level(datetime(2019,8,1), 19, player_1)
    level_2_1 = Level(datetime(2019,8,1), 23, player_2)

    player_1.levels
    player_2.levels

    session = Session()
    session.add(player_1)
    session.add(player_2)

    session.add(level_1_1)
    session.add(level_1_2)
    session.add(level_2_1)

    session.commit()
    session.close()

