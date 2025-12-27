from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.album_repository import AlbumRepository
from src.controllers.album_finder_controller import AlbumFinderController
from src.views.album_finder_view import AlbumFinderView

def album_finder_composer():
    model = AlbumRepository(db_connection_handler)
    controller = AlbumFinderController(model)
    view = AlbumFinderView(controller)

    return view
