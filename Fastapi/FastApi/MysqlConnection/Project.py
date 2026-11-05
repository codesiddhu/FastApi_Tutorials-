from fastapi import FastAPI,Depends
from pydantic import BaseModel
from Models import Book2
from sqlalchemy.orm import session
from Database import get,new_engine

app = FastAPI()

class BookStore(BaseModel):
    id:int
    title :str
    author :str
    publish_date :str

@app.post("/books")
def book(book:BookStore,db:session = Depends(get)):
    newBook = Book2(id=book.id,title = book.title,author =book.author,publish_date = book.publish_date)
    db.add(newBook)
    db.commit()
    db.refresh(newBook)
    return newBook
