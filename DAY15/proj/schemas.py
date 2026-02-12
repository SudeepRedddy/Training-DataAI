from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    price: float

class UserSchema(BaseModel):
    username: str
    password: str
