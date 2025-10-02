from fastapi import FastAPI
from app.core.database import database
from app.interfaces.routes.genre_route import router as genre_router
from app.interfaces.routes.oeuvre_route import router as oeuvre_router

def create_app() -> FastAPI:
    """
    Crée et configure l'application FastAPI.

    Returns:
        FastAPI: L'instance de l'application configurée.
    """
    app = FastAPI(title="BooksToScrape")
    app.include_router(genre_router)
    app.include_router(oeuvre_router)
    
    @app.on_event("startup")
    async def on_startup():
        """
        Événement de démarrage de l'application.
        Initialise la base de données.
        """
        await database.init_db()
    
    return app
