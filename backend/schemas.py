from pydantic import BaseModel
from typing import List, Optional

class HadithBase(BaseModel):
    id: int
    text: str
    sharh: Optional[str] = None
    chapter: Optional["ChapterBase"] = None
    book: Optional["BookBase"] = None
    collection: Optional["CollectionBase"] = None

    class Config:
        orm_mode = True

class ChapterBase(BaseModel):
    id: int
    name: str
    hadiths: List[HadithBase] = []

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    id: int
    name: str
    pages: Optional[int] = None
    chapters: List[ChapterBase] = []

    class Config:
        orm_mode = True

class CollectionBase(BaseModel):
    id: int
    name: str
    books: List[BookBase] = []

    class Config:
        orm_mode = True
