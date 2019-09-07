from datetime import datetime
from .entities.entity import Base, Session, engine
from .entities.player import Player, Level
from .entities.game import Game, GameDetails


if __name__ == "__main__":

    from datetime import datetime, time
    Base.metadata.create_all(engine)

    player_1 = Player("Antoine", "Rosin")
    player_2 = Player("Guillaume", "Rosin")

    level_1_1 = Level(player_1, datetime(2019,7,1), 15)
    level_1_2 = Level(player_1, datetime(2019,8,1), 19)
    level_2_1 = Level(player_2, datetime(2019,8,1), 23)

    player_1.levels
    player_2.levels

    game_1 = Game("tamarin", "not_known", datetime(2019,9, 10))
    game_details_1 = GameDetails(game_1, max_hcp_man=13, tee_off=time(11,30), fee=200)

    game_1.game_details.max_hcp_woman

    session = Session()
    session.add(player_1)
    session.add(player_2)

    session.add(level_1_1)
    session.add(level_1_2)
    session.add(level_2_1)

    session.add(game_1)
    session.add(game_details_1)
    
    session.commit()
    session.close()