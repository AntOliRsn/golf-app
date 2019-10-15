# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flasgger import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from backend.config import cfg

cors = CORS()
db = SQLAlchemy()
ma = Marshmallow()
spec = APISpec(
    title=cfg.APISPEC['title'],
    version=cfg.APISPEC['version'],
    openapi_version=cfg.APISPEC['openapi_version'],
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)
