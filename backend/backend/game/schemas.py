from backend.extensions import ma
from backend.game.classes import Game, GameDetails


class GameSchema(ma.ModelSchema):

    game_details = ma.Nested(
        "GameDetailsSchema", exclude=("id", )
    )

    draw_groups = ma.Nested(
        "DrawGroupSchema",
        many=True,
        exclude=("id", )
    )

    class Meta:
        model = Game
        dump_only = ("id", )


class GameDetailsSchema(ma.ModelSchema):

    game = ma.Nested(
        "GameSchema", only=("id", "golf", "game_date")
    )

    class Meta:
        model = GameDetails
        dump_only = ("id", )


game_schema = GameSchema()
game_details_schema = GameDetailsSchema()