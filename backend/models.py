from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db import Base

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="collection")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    pages = Column(Integer)
    collection_id = Column(Integer, ForeignKey("collections.id"))
    collection = relationship("Collection", back_populates="books")
    chapters = relationship("Chapter", back_populates="book")

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="chapters")
    hadiths = relationship("Hadith", back_populates="chapter")

class Hadith(Base):
    __tablename__ = "hadiths"
    id = Column(Integer, primary_key=True, index=True)
    arabic_text = Column(Text, nullable=False)
    english_text = Column(Text, nullable=False)
    sharh = Column(Text)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    chapter = relationship("Chapter", back_populates="hadiths")

    # Direct link to collection through book -> chapter
    collection_id = Column(Integer, ForeignKey("collections.id"))
    collection = relationship("Collection")

    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book")
