from src.controllers.interfaces.photo_deleter_controller import PhotoDeleterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PhotoDeleterView(ViewInterface):
    def __init__(self, controller: PhotoDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        photo_id = http_request.param["photo_id"]
        self.__controller.delete_photo(photo_id)

        return HttpResponse(status_code=204)
