from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.album_repository import AlbumRepository
from src.controllers.album_lister_controller import AlbumListerController
from src.views.album_lister_view import AlbumListerView

def album_lister_composer():
    model = AlbumRepository(db_connection_handler)
    controller = AlbumListerController(model)
    view = AlbumListerView(controller)

    return view
