from backend.extensions import ma
from backend.draw_group.classes import DrawGroup


class DrawGroupSchema(ma.ModelSchema):

    players = ma.Nested(
        "PlayerSchema",
        many=True,
        only=("id", "first_name", "last_name")
    )

    game = ma.Nested(
        "GameSchema", only=("id", "golf", "game_date")
    )

    class Meta:
        model = DrawGroup
        dump_only = ("id", )


draw_group_schema = DrawGroupSchema()
