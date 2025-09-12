from src.models.sqlite.interfaces.album_repository import AlbumRepositoryInterface
from .interfaces.album_deleter_controller import AlbumDeleterControllerInterface

class AlbumDeleterController(AlbumDeleterControllerInterface):
    def __init__(self, album_repository: AlbumRepositoryInterface) -> None:
        self.__album_repository = album_repository

    def delete_album(self, album_id: int) -> None:
        self.__album_repository.delete_album(album_id)
