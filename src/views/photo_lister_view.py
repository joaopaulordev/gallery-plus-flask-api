from src.controllers.interfaces.photo_lister_controller import PhotoListerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PhotoListerView(ViewInterface):
    def __init__(self, controller: PhotoListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_photos()
        return HttpResponse(status_code=200, body=body_response)
