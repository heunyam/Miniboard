import os


class LocalLevelConfig:
    ENV = "development"
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", "34c145a1db56f6e2ce104ca78c6a102")


class ProductionLevelConfig:
    ENV = "production"
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")