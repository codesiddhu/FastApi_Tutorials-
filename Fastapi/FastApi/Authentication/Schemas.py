from pydantic import EmailStr,BaseModel

class User_Regestration(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:str

class User_Login(BaseModel):
    username:str
    password:str
