from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import noload, selectinload
from db import SessionLocal
from models import Collection, Book, Hadith, Chapter
from schemas import CollectionBase, BookBase, HadithBase, ChapterBase

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get(
    "/collections",
    response_model=List[CollectionBase],
    summary="List all collections (IDs and names)",
    description="Returns a flat list of collection objects containing only id and name fields.",
    tags=["Hadith"]
)
async def list_collections(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Collection).options(noload("*")))
    collections = result.scalars().all()
    return collections

@router.get(
    "/collections/{collection_id}/books",
    response_model=List[BookBase],
    summary="List books in a collection by collection ID",
    description="Given a collection_id, returns all books belonging to that collection.",
    tags=["Hadith"],
    responses={404: {"description": "Collection not found"}}
)
async def list_books_by_collection(
    collection_id: int = Path(..., description="ID of the collection", ge=1),
    db: AsyncSession = Depends(get_db),
):
    # Ensure the collection exists
    collection = await db.get(Collection, collection_id, options=(noload("*"),))
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    result = await db.execute(select(Book).options(noload("*")).where(Book.collection_id == collection_id))
    books = result.scalars().all()
    return books

@router.get(
    "/books/{book_id}/chapters",
    response_model=List[ChapterBase],
    summary="List chapters of a book by book ID",
    description="Given a book_id, returns all chapters belonging to that book, including their hadiths.",
    tags=["Hadith"],
    responses={404: {"description": "Book not found"}}
)
async def list_chapters_by_book(
    book_id: int = Path(..., description="ID of the book", ge=1),
    db: AsyncSession = Depends(get_db),
):
    # Ensure the book exists
    book = await db.get(Book, book_id, options=(noload("*"),))
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    result = await db.execute(
        select(Chapter).options(selectinload(Chapter.hadiths)).where(Chapter.book_id == book_id)
    )
    chapters = result.scalars().unique().all()
    return chapters

@router.get(
    "/chapters/{chapter_id}/hadiths",
    response_model=List[HadithBase],
    summary="List hadiths of a chapter by chapter ID",
    description="Given a chapter_id, returns all hadiths belonging to that chapter.",
    tags=["Hadith"],
    responses={404: {"description": "Chapter not found"}}
)
async def list_hadiths_by_chapter(
    chapter_id: int = Path(..., description="ID of the chapter", ge=1),
    db: AsyncSession = Depends(get_db),
):
    # Ensure the chapter exists
    chapter = await db.get(Chapter, chapter_id, options=(noload("*"),))
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")

    result = await db.execute(select(Hadith).options(noload("*")).where(Hadith.chapter_id == chapter_id))
    hadiths = result.scalars().all()
    return hadiths
