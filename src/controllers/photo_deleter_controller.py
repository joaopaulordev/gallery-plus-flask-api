from src.models.sqlite.interfaces.photo_repository import PhotoRepositoryInterface
from .interfaces.photo_deleter_controller import PhotoDeleterControllerInterface

class PhotoDeleterController(PhotoDeleterControllerInterface):
    def __init__(self, photo_repository: PhotoRepositoryInterface) -> None:
        self.__photo_repository = photo_repository

    def delete_photo(self, photo_id: int) -> None:
        self.__photo_repository.delete_photo(photo_id)
