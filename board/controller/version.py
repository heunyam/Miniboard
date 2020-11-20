from board.model import session
from board.model.android_info import AndroidInfo


def check_recently_version(android_version):

    current_version = session.query(AndroidInfo).order_by(AndroidInfo.created_at.desc()).first()

    return {
        'is_lastest': True if android_version == current_version else False
    }