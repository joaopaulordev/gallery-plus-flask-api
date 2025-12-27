from src.controllers.interfaces.photo_finder_controller import PhotoFinderControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PhotoFinderView(ViewInterface):
    def __init__(self, controller: PhotoFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        photo_id = http_request.param["photo_id"]
        body_response = self.__controller.find_photo_by_id(photo_id)

        return HttpResponse(status_code=200, body=body_response)
