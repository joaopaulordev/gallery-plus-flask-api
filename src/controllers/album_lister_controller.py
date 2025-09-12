from src.models.sqlite.interfaces.album_repository import AlbumRepositoryInterface
from src.models.sqlite.entities.album import AlbumTable
from .interfaces.album_lister_controller import AlbumListerControllerInterface

class AlbumListerController(AlbumListerControllerInterface):
    def __init__(self, album_repository: AlbumRepositoryInterface) -> None:
        self.__album_repository = album_repository

    def list_albums(self) -> dict:
        albums = self.__get_albums_in_db()
        response = self.__format_response(albums)
        return response

    def __get_albums_in_db(self) -> list[AlbumTable]:
        albums = self.__album_repository.get_albums()
        return albums

    def __format_response(self, albuns: list[AlbumTable]) -> dict:
        return [album.to_dict() for album in albuns]

