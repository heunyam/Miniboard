from board.model import session
from board.model.post import Post


def post(title, content):
    new_post = Post(title=title, content=content)

    session.add(new_post)
    session.commit()

    return {
        "message": "posting Successfully"
    }
