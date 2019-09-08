# coding=utf-8

import yaml


class ConfigurationFromEnv:

    def __init__(self, env_config_path):

        env_config = yaml.safe_load(open(env_config_path))

        self.SQLALCHEMY_DATABASE_URI = (
            "postgresql://{user}:{pw}@{host}:{port}/{db}".format(
                user=env_config['project-database']["user"],
                pw=env_config['project-database']["password"],
                db=env_config['project-database']["name"],
                host=env_config['project-database']["hostname"],
                port=env_config['project-database']["port"]
            )
        )


# Temporary for dev mode
env_config_path = "backend/config.yaml"
cfg = ConfigurationFromEnv(env_config_path)