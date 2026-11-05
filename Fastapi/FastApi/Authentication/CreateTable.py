from database import Base,get_db,new_engine
from Models import User

Base.metadata.create_all(bind =new_engine)


print("created successfully here ............")
