from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}  # Add this line

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)

    posts = relationship("Post", order_by="Post.id", back_populates="user")
