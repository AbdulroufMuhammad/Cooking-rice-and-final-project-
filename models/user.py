from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, Column , Boolean , Integer,ForeignKey

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    Id = Column(Integer,primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String, unique=True)
    Password = Column(String )




    