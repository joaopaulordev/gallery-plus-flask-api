from abc import ABC, abstractmethod
from src.models.sqlite.entities.photo import PhotoTable


class PhotoRepositoryInterface(ABC):

    @abstractmethod
    def create_photo(self, photo: PhotoTable) -> None:
        pass

    @abstractmethod
    def get_photo_by_id(self, photo_id: int) -> PhotoTable:
        pass


    @abstractmethod
    def get_photos(self) -> list[PhotoTable]:
        pass

    
    @abstractmethod
    def delete_photo(self, photo_id: int) -> None:
        pass