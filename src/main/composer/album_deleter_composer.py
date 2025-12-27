from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.album_repository import AlbumRepository
from src.controllers.album_deleter_controller import AlbumDeleterController
from src.views.album_deleter_view import AlbumDeleterView

def album_deleter_composer():
    model = AlbumRepository(db_connection_handler)
    controller = AlbumDeleterController(model)
    view = AlbumDeleterView(controller)

    return view
