from src.controllers.interfaces.album_lister_controller import AlbumListerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class AlbumListerView(ViewInterface):
    def __init__(self, controller: AlbumListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_albums()
        return HttpResponse(status_code=200, body=body_response)
