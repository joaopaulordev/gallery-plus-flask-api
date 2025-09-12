from src.models.sqlite.interfaces.photo_repository import PhotoRepositoryInterface
from src.models.sqlite.entities.photo import PhotoTable
from .interfaces.photo_lister_controller import PhotoListerControllerInterface

class PhotoListerController(PhotoListerControllerInterface):
    def __init__(self, photo_repository: PhotoRepositoryInterface) -> None:
        self.__photo_repository = photo_repository

    def list_photos(self) -> dict:
        photos = self.__get_photos_in_db()
        response = self.__format_response(photos)
        return response

    def __get_photos_in_db(self) -> list[PhotoTable]:
        photos = self.__photo_repository.get_photos()
        return photos

    def __format_response(self, photos: list[PhotoTable]) -> dict:
        return [photo.to_dict() for photo in photos]

