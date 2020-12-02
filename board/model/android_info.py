from sqlalchemy import Column, String, Integer, TIMESTAMP, text
from board.model import Base


class AndroidInfo(Base):
    __tablename__ = 'android_infos'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    version = Column(String(10), primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
