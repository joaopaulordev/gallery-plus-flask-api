from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.photo_repository import PhotoRepository
from src.controllers.photo_lister_controller import PhotoListerController
from src.views.photo_lister_view import PhotoListerView

def photo_lister_composer():
    model = PhotoRepository(db_connection_handler)
    controller = PhotoListerController(model)
    view = PhotoListerView(controller)

    return view
