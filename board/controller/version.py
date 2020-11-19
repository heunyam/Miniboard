from board.model import mongodb


def check_recently_version(android_version):
    current_version = mongodb.android_info.find()[0]['version']

    return {
        'is_lastest': True if android_version == current_version else False
    }