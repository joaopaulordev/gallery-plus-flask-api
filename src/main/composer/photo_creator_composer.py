from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.photo_repository import PhotoRepository
from src.controllers.photo_creator_controller import PhotoCreatorController
from src.views.photo_creator_view import PhotoCreatorView

def photo_creator_composer():
    model = PhotoRepository(db_connection_handler)
    controller = PhotoCreatorController(model)
    view = PhotoCreatorView(controller)

    return view
