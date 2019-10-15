# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


cors = CORS()
db = SQLAlchemy()
ma = Marshmallow()
