from src.controllers.interfaces.photo_creator_controller import PhotoCreatorControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PhotoCreatorView(ViewInterface):
    def __init__(self, controller: PhotoCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:        
        photo_info = http_request.body
        body_response = self.__controller.create_photo(photo_info)

        return HttpResponse(status_code=201, body=body_response)
