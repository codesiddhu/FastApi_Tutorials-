from Database import Base,new_engine
from Models import Book2

Base.metadata.create_all(bind = new_engine)
