from database import Database
from model import BookModel

db = Database(database="relatorio5", collection="book")
db.resetDatabase()
book_model = BookModel(db)

id_book = book_model.create_book("Os três mosqueteiros", "Pedro Guimarães", 1995)

book_model.read_book_by_id(id_book)
book_model.update_book(id_book, "Os três mosqueteiros","Pedro Guimarães", 1890)
book_model.delete_book(id_book)