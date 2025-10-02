from fastapi import FastAPI, Depends
from app.core.database import database
from app.interfaces.routes.genre_route import router as genre_router
from app.interfaces.routes.oeuvre_route import router as oeuvre_router


def create_app() -> FastAPI:
    app = FastAPI(title="BooksToScrape")
    app.include_router(genre_router)
    app.include_router(oeuvre_router)
    
    @app.on_event("startup")
    async def on_startup():
        # initialise la base de données au démarrage
        await database.init_db()
    return app








