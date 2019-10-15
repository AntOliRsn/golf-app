from backend.extensions import ma
from backend.player.classes import Player, Level


class PlayerSchema(ma.ModelSchema):

    levels = ma.Nested(
        "LevelSchema", many=True,
        only=("date_valid", "level")
    )

    draw_groups = ma.Nested(
        "DrawGroupSchema", many=True,
        only=("id", "game")
    )

    class Meta:
        model = Player
        dump_only = ("id", )


class LevelSchema(ma.ModelSchema):

    player = ma.Nested(
        "PlayerSchema", only=("id", "first_name", "last_name")
    )

    class Meta:
        model = Level
        dump_only = ("id", )


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

level_schema = LevelSchema()