from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    inventory = Column(Integer, default=0)
    issues = relationship("Issue", back_populates="book")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    issued_books = relationship("Issue", back_populates="student")

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, index=True)
    book_id = Column(Integer, index=True)
    issued_at = Column(DateTime, default=datetime.utcnow)
    student = relationship("Student", back_populates="issued_books")
    book = relationship("Book", back_populates="issues")