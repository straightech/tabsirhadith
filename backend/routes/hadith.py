from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db import SessionLocal
from models import Collection, Book, Hadith
from schemas import CollectionBase, BookBase, HadithBase

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/collections", response_model=list[CollectionBase])
async def get_collections(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Collection))
    return result.scalars().all()

@router.get("/collection/{id}", response_model=list[BookBase])
async def get_collection(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book).where(Book.collection_id == id))
    books = result.scalars().all()
    if not books:
        raise HTTPException(status_code=404, detail="Collection not found or has no books")
    return books

@router.get("/book/{id}", response_model=list[HadithBase])
async def get_book(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Hadith).join(Book.chapters).where(Book.id == id))
    hadiths = result.scalars().all()
    if not hadiths:
        raise HTTPException(status_code=404, detail="Book not found or has no hadiths")
    return hadiths

@router.get("/hadith/{id}", response_model=HadithBase)
async def get_hadith(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Hadith).where(Hadith.id == id))
    hadith = result.scalar_one_or_none()
    if not hadith:
        raise HTTPException(status_code=404, detail="Hadith not found")
    return hadith
