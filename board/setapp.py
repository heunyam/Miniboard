from flask import Flask
from board.router import bp


def create_app(*config_cls):

    # 해석 못함
    config_cls = [
        config() if isinstance(config, type) else config for config in config_cls
    ]

    _app = Flask(__name__)
    _app.register_blueprint(bp)

    for config in config_cls:
        _app.config.from_object(config)

    return _app
