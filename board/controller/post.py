from board.model import session
from board.model.post import Post
from flask import abort


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


def delete_post(post_id):
    post = session.query(Post).filter(Post.id == post_id).first()

    if post:
        session.delete(post)
        session.commit()
    else:
        return abort(404, f"The {post_id} is no corresponding post")

    return {
        "message": "Sucessfully deleted"
    }


def modify_post(post_id, title, content):
    post = session.query(Post).filter(Post.id == post_id).first()

    if post:
        post.title = title
        post.content = content
        session.commit()
    else:
        return abort(404, f"The {post_id} is no corresponding post")

    return {
        "message": "Sucessfully modifying"
    }
