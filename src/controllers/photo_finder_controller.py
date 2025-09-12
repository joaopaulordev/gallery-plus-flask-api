from src.models.sqlite.interfaces.photo_repository import PhotoRepositoryInterface
from src.models.sqlite.entities.photo import PhotoTable
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.photo_finder_controller import PhotoFinderControllerInterface


class PhotoFinderController(PhotoFinderControllerInterface):
    def __init__(self, photo_repository: PhotoRepositoryInterface) -> None:
        self.__photo_repository = photo_repository

    def find_photo_by_id(self, photo_id: int) -> dict:
        photo = self.__find_photo_in_db(photo_id)
        response = self.__format_response(photo)
        return response

    def __find_photo_in_db(self, photo_id: int) -> PhotoTable:
        photo = self.__photo_repository.get_photo_by_id(photo_id)
        if not photo:
            raise HttpNotFoundError("Foto não encontrada!")

        return photo

    def __format_response(self, photo: PhotoTable) -> dict:
        return {
            "id": photo.id,
            "title": photo.title,
            "albumsIds": [],
            "imageId": photo.imageId,
            "albums": [album.to_dict() for album in photo.albums],
            "nextPhotoId": 11,
            "previousPhotoId": 0
        }

