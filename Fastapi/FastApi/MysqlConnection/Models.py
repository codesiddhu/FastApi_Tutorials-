from Database import Base
from sqlalchemy import Column,Integer,VARCHAR


class Book2(Base):
    __tablename__="Books2"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(255))
    author = Column(VARCHAR(255))
    publish_date = Column(VARCHAR(255))

