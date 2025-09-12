from src.models.sqlite.interfaces.album_repository import AlbumRepositoryInterface
from src.models.sqlite.entities.album import AlbumTable
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.album_finder_controller import AlbumFinderControllerInterface


class AlbumFinderController(AlbumFinderControllerInterface):
    def __init__(self, album_repository: AlbumRepositoryInterface) -> None:
        self.__album_repository = album_repository
        
    def find_album_by_id(self, album_id: int) -> dict:
    
        album = self.__find_album_in_db(album_id)
        response = self.__format_response(album)
        return response

    def __find_album_in_db(self, album_id: int) -> AlbumTable:
        album = self.__album_repository.get_album_by_id(album_id)
        if not album:
            raise HttpNotFoundError("Album não encontrado!")

        return album

    def __format_response(self, album: AlbumTable) -> dict:
        return album.to_dict()
