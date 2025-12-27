from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.album_repository import AlbumRepository
from src.controllers.album_creator_controller import AlbumCreatorController
from src.views.album_creator_view import AlbumCreatorView

def album_creator_composer():
    model = AlbumRepository(db_connection_handler)
    controller = AlbumCreatorController(model)
    view = AlbumCreatorView(controller)

    return view
