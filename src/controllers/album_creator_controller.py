from src.models.sqlite.interfaces.album_repository import AlbumRepositoryInterface
from .interfaces.album_creator_controller import AlbumCreatorControllerInterface
from src.models.sqlite.entities.album import AlbumTable


class AlbumCreatorController(AlbumCreatorControllerInterface):
    def __init__(self, album_repository: AlbumRepositoryInterface) -> None:
        self.__album_repository = album_repository

    def create_album(self, album_info: dict) -> dict:
        title = album_info["title"]

        new_album = AlbumTable(title=title)

        self.__insert_album_in_db(new_album)

        formated_response = self.__format_response(new_album)
        return formated_response
    

    def __insert_album_in_db(self, album: AlbumTable) -> None:
        self.__album_repository.create_album(album)


    def __format_response(self, album: AlbumTable) -> dict:
        return album.to_dict()
