from pydantic import BaseModel, Field
from typing import Optional, List

# ========== RESPONSE SCHEMAS (used by GET endpoints) ==========
# These mirror the DB models and are optimized for read operations and auto-generated docs.

class CollectionBase(BaseModel):
    id: int = Field(..., description="Unique identifier of the collection", example=1)
    name: str = Field(..., description="Name of the collection", example="Sahih al-Bukhari")

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    id: int = Field(..., description="Unique identifier of the book", example=10)
    name: str = Field(..., description="Name of the book", example="Book of Revelation")
    visible_id: Optional[int] = Field(None, description="Human-friendly visible ID for the book", example=1)
    pages: Optional[int] = Field(None, description="Number of pages if known", example=320)
    collection_id: Optional[int] = Field(None, description="Foreign key to the parent collection", example=1)

    class Config:
        orm_mode = True


class HadithBase(BaseModel):
    id: int = Field(..., description="Unique identifier of the hadith", example=1000)
    arabic_text: str = Field(..., description="Arabic text of the hadith", example="إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ")
    english_text: str = Field(..., description="English translation of the hadith", example="Actions are judged by intentions")
    sharh: Optional[str] = Field(None, description="Commentary (Sharh) if available")
    chapter_id: int = Field(..., description="Foreign key to the parent chapter", example=100)
    book_id: Optional[int] = Field(None, description="Foreign key to the parent book (redundant for quick access)", example=10)
    collection_id: Optional[int] = Field(None, description="Foreign key to the parent collection (redundant for quick access)", example=1)

    class Config:
        orm_mode = True


class ChapterBase(BaseModel):
    id: int = Field(..., description="Unique identifier of the chapter", example=100)
    name: str = Field(..., description="Name of the chapter", example="Chapter on Faith")
    book_id: int = Field(..., description="Foreign key to the parent book", example=10)
    hadiths: List[HadithBase] = Field(default_factory=list, description="List of hadiths belonging to this chapter")

    class Config:
        orm_mode = True


# ========== REQUEST SCHEMAS (for future POST/PUT use) ==========
# Not used by current GET endpoints but defined for completeness and better docs.

class CollectionCreate(BaseModel):
    name: str = Field(..., description="Name of the collection", example="Sahih Muslim")


class BookCreate(BaseModel):
    name: str = Field(..., description="Name of the book", example="Book of Prayer")
    visible_id: Optional[int] = Field(None, description="Human-friendly visible ID for the book", example=2)
    pages: Optional[int] = Field(None, description="Number of pages if known", example=280)
    collection_id: int = Field(..., description="Parent collection ID", example=1)


class ChapterCreate(BaseModel):
    name: str = Field(..., description="Name of the chapter", example="Chapter on Ablution")
    book_id: int = Field(..., description="Parent book ID", example=10)


class HadithCreate(BaseModel):
    arabic_text: str = Field(..., description="Arabic text of the hadith")
    english_text: str = Field(..., description="English translation of the hadith")
    sharh: Optional[str] = Field(None, description="Commentary (Sharh) if available")
    chapter_id: int = Field(..., description="Parent chapter ID", example=100)
    book_id: Optional[int] = Field(None, description="Parent book ID (optional if resolvable from chapter)", example=10)
    collection_id: Optional[int] = Field(None, description="Parent collection ID (optional if resolvable)", example=1)
