from fastapi import status,HTTPException,Depends,FastAPI
import utils,Models,Schemas
from sqlalchemy.orm import Session
from database import get_db
from jose import jwt
from datetime import datetime,timedelta


from fastapi.security import OAuth2PasswordRequestForm



SECRET_KEY = "z4mqxFi5zCX5VX1Iz21i3fATELuc3Ire8kXttDC1OJc"
ALGORITHOM = "HS256"
ACESS_TOKEN_EMPIRE_MINUTES = 30

app = FastAPI()

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EMPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHOM)
    return encode_jwt


@app.post("/")
def signup(user: Schemas.User_Regestration, db: Session = Depends(get_db)):

    exit_user = db.query(Models.User).filter(
        Models.User.username == user.username
    ).first()

    if exit_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    hass_pass = utils.hass_password(user.password)

    new_user = Models.User(
        username=user.username,
        email=user.email,
        password=hass_pass,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role
    }


@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(Models.User).filter(Models.User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")

    if not utils.verify_password(form_data.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid password")
    token_data = {
    "sub": user.username,
    "role": user.role,
    "email": user.email
}
    token =create_access_token(token_data)
    return {
        "access_token":token,
        "token_type": "bearer"
    }