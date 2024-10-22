from schema.user import UserCreate
from models.user import User, SessionLocal, Base, engine  
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends


app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/usr/signup')
async def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(FirstName=user.FirstName, LastName=user.LastName, Email=user.Email, Password=user.Password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user