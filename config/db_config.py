import os


DB_NAME = "board"


class LocalDBConfig:
    DB_URL = f"mysql+mysqldb://root:heunyam@localhost:3306/{DB_NAME}?charset=utf8"


class RemoteDBConfig:
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_ENDPOINT = os.getenv('DB_ENDPOINT')
    DB_URL = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_ENDPOINT}:3306/{DB_NAME}?charset=utf8"
