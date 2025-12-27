from src.models.sqlite.interfaces.album_repository import AlbumRepositoryInterface
from .interfaces.album_deleter_controller import AlbumDeleterControllerInterface
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.models.sqlite.entities.album import AlbumTable


class AlbumDeleterController(AlbumDeleterControllerInterface):
    def __init__(self, album_repository: AlbumRepositoryInterface) -> None:
        self.__album_repository = album_repository

    def delete_album(self, album_id: int) -> None:
        self.__find_album_in_db(album_id)        

        self.__album_repository.delete_album(album_id)
        

    def __find_album_in_db(self, album_id: int) -> AlbumTable:
        album = self.__album_repository.get_album_by_id(album_id)
        if not album:
            raise HttpNotFoundError("Album não encontrado!")

        return album

        
