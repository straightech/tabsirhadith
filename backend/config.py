import os

class Settings:
    def __init__(self):
        self.environment = os.getenv("ENV", "development")
        if self.environment == "production":
            self.database_url = os.getenv(
                "DATABASE_URL",
                "postgresql+asyncpg://postgres:postgres@db:5432/appdb"
            )
        else:
            self.database_url = os.getenv(
                "DATABASE_URL",
                "sqlite+aiosqlite:///./dev.db"
            )

settings = Settings()
