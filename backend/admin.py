from sqladmin import ModelView
from models import Collection, Book, Chapter, Hadith

class CollectionAdmin(ModelView, model=Collection):
    column_list = [Collection.id, Collection.name]

class BookAdmin(ModelView, model=Book):
    column_list = [Book.id, Book.name, Book.pages, Book.collection_id]

class ChapterAdmin(ModelView, model=Chapter):
    column_list = [Chapter.id, Chapter.name, Chapter.book_id]

class HadithAdmin(ModelView, model=Hadith):
    column_list = [Hadith.id, Hadith.arabic_text, Hadith.english_text, Hadith.sharh, Hadith.chapter_id]
