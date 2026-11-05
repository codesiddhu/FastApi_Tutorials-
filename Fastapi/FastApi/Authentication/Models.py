from database import Base,new_engine
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(255),unique = True)
    email = Column(String(255),unique=True)
    password = Column(String(255))
    role = Column(String(255),default = "user")
    
