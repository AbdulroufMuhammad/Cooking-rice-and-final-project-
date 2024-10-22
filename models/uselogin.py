from models.user import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from models.user import User

class UserLogin(Base):
    __tablename__ = "userlogin"

    Id = Column(Integer, primary_key=True)
    Email = Column(String, ForeignKey("users.Email"), unique=True)
    Password = Column(String)