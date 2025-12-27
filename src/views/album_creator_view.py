from src.controllers.interfaces.album_creator_controller import AlbumCreatorControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class AlbumCreatorView(ViewInterface):
    def __init__(self, controller: AlbumCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:        
        album_info = http_request.body
        body_response = self.__controller.create_album(album_info)

        return HttpResponse(status_code=201, body=body_response)
