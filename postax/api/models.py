from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column()