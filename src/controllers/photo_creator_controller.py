from src.models.sqlite.interfaces.photo_repository import PhotoRepositoryInterface
from .interfaces.photo_creator_controller import PhotoCreatorControllerInterface
from src.models.sqlite.entities.photo import PhotoTable


class PhotoCreatorController(PhotoCreatorControllerInterface):
    def __init__(self, photo_repository: PhotoRepositoryInterface) -> None:
        self.__photo_repository = photo_repository

    def create_photo(self, photo_info: dict) -> dict:
        title = photo_info["title"]

        new_photo = PhotoTable(title=title)

        self.__insert_photo_in_db(new_photo)

        formated_response = self.__format_response(new_photo)
        return formated_response
    

    def __insert_photo_in_db(self, photo: PhotoTable) -> None:
        self.__photo_repository.create_photo(photo)


    def __format_response(self, photo: PhotoTable) -> dict:
        return {
            "id": photo.id,
            "title": photo.title,
            "albumsIds": [album.to_dict() for album in photo.albums]
        }

