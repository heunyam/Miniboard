from board.model import session
from board.model.post import Post


def post(title, content):
    new_post = Post(title=title, content=content)

    session.add(new_post)
    session.commit()

    return {
        "message": "posting Successfully"
    }


def get_posts():
    posts = session.query(Post).order_by(Post.created_at.desc()).all()

    return {
        "posts": [{
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": str(post.created_at)
        } for post in posts]
    }
