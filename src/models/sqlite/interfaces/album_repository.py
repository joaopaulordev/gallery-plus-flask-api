from abc import ABC, abstractmethod
from src.models.sqlite.entities.album import AlbumTable


class AlbumRepositoryInterface(ABC):

    @abstractmethod
    def create_album(self, album: AlbumTable) -> None:
        pass

    @abstractmethod
    def get_album_by_id(self, album_id: int) -> AlbumTable:
        pass


    @abstractmethod
    def get_albums(self) -> list[AlbumTable]:
        pass

    
    @abstractmethod
    def delete_album(self, album_id: int) -> None:
        pass