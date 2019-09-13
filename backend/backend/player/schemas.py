from backend.extensions import ma
from backend.player.classes import Player, Level


class PlayerSchema(ma.ModelSchema):

    levels = ma.Nested(
        "LevelSchema", many=True,
        only=("date_valid", "level")
    )

    dump_only = ("first_name", "levels")

    class Meta:
            model = Player


class LevelSchema(ma.ModelSchema):
    class Meta:
        model = Level


player_schema = PlayerSchema()
