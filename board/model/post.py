from sqlalchemy import Column, String, Integer, TIMESTAMP, text
from board.model import Base


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(45), nullable=False)
    content = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
