from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.photo_repository import PhotoRepository
from src.controllers.photo_deleter_controller import PhotoDeleterController
from src.views.photo_deleter_view import PhotoDeleterView

def photo_deleter_composer():
    model = PhotoRepository(db_connection_handler)
    controller = PhotoDeleterController(model)
    view = PhotoDeleterView(controller)

    return view
