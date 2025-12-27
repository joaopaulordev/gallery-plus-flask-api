from src.controllers.interfaces.album_deleter_controller import AlbumDeleterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class AlbumDeleterView(ViewInterface):
    def __init__(self, controller: AlbumDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        album_id = http_request.param["album_id"]
        self.__controller.delete_album(album_id)

        return HttpResponse(status_code=204)
