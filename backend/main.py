from fastapi import FastAPI
from fastapi import FastAPI
from sqladmin import Admin
from db import engine, Base
from admin import CollectionAdmin, BookAdmin, ChapterAdmin, HadithAdmin
from routes.root import router as root_router
from routes.hadith import router as hadith_router

# FastAPI app
app = FastAPI()

# SQLAdmin setup
admin = Admin(app, engine)
admin.add_view(CollectionAdmin)
admin.add_view(BookAdmin)
admin.add_view(ChapterAdmin)
admin.add_view(HadithAdmin)

# Include routes
app.include_router(root_router)
app.include_router(hadith_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
