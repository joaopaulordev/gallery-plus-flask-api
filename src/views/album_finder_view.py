from src.controllers.interfaces.album_finder_controller import AlbumFinderControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class AlbumFinderView(ViewInterface):
    def __init__(self, controller: AlbumFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        album_id = http_request.param["album_id"]
        body_response = self.__controller.find_album_by_id(album_id)

        return HttpResponse(status_code=200, body=body_response)
