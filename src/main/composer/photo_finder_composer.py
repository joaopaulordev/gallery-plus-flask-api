from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.photo_repository import PhotoRepository
from src.controllers.photo_finder_controller import PhotoFinderController
from src.views.photo_finder_view import PhotoFinderView

def photo_finder_composer():
    model = PhotoRepository(db_connection_handler)
    controller = PhotoFinderController(model)
    view = PhotoFinderView(controller)

    return view
