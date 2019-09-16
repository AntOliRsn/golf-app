# Declare models from other submodules to avoid schema importing errors
from backend.game.schemas import GameSchema, GameDetailsSchema
from backend.player.schemas import PlayerSchema, LevelSchema