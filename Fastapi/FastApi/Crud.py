from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from fastapi import status
app = FastAPI()

books = [
    {
        "id":1,
        "Tittle":"The Lion",
        "Author":"siddhu",
        "Publish_date":"1999-05-29"
    },
    {
        "id":2,
        "Tittle":"Jurasic Park",
        "Author":"sreedhar",
        "Publish_date":"2002-10-19"
    },
    {
        "id":3,
        "Tittle":"Fox",
        "Author":"Daniel",
        "Publish_date":"2010-11-30"
    }
]

@app.get("/")
def home():
    return {"message":"hello world"}

@app.get("/books")
def books_data():
    return books

class Book(BaseModel):
    id:int
    Tittle:str
    Author:str
    Publish_date:str

@app.post("/books")
def create_book(book:Book):
    new_book=book.model_dump()
    books.append(new_book)
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found") 

class Book_update(BaseModel):
    Tittle:str
    Author:str
    Publish_date:str
@app.put("/books/{book_id}")
def book_update(book_id:int,book_update:Book_update):
    for book in books:
        if book['id']==book_id:
            book["Tittle"] =book_update.Tittle
            book["Author"] = book_update.Author
            book["Publish_date"] = book_update.Publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove (book)
            return {"message":"book is deleted"}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
