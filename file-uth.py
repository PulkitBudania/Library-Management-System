from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
import models, schemas

app = FastAPI()

# Your database connection here
engine = create_engine('sqlite:///./library.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.post('/books/', response_model=models.Book)
def add_book(book: schemas.BookCreate, db: Session = Depends(SessionLocal)):
    # Add book logic here

  @app.post('/students/', response_model=models.Student)
  def add_student(student: schemas.StudentCreate, db: Session = Depends(SessionLocal)):
    # Add student logic here

   @app.put('/books/{book_id}/inventory', response_model=models.Book)
   def update_inventory(book_id: int, inventory: schemas.InventoryUpdate, db: Session = Depends(SessionLocal)):
    # Update inventory logic here

    @app.post('/students/{student_id}/issue', response_model=models.Issue)
    def issue_book(student_id: int, book_id: int, db: Session = Depends(SessionLocal)):
    # Issue book logic here

     @app.post('/students/{student_id}/return', response_model=models.Issue)
     def return_book(student_id: int, book_id: int, db: Session = Depends(SessionLocal)):
    # Return book logic here

      @app.get('/popular_books/', response_model=list[schemas.PopularBook])
      def popular_books(db: Session = Depends(SessionLocal)):
    # Popular books logic here
       popular_books = db.query(models.Book, func.count(models.Issue.book_id).label('issues_count')).join(models.Issue, models.Book.id == models.Issue.book_id).group_by(models.Book.id).order_by('issues_count DESC').all()
       return [schemas.PopularBook(id=book.id, title=book.title, author=book.author, issues_count=book.issues_count) for book, issues_count in popular_books]