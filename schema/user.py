from pydantic import BaseModel


class UserCreate(BaseModel):

    Id : int
    Email : str
    FirstName : str
    LastName : str
    Password : str




class UserLogin(BaseModel):
    Id : int
    Email : str
    Password : str
    