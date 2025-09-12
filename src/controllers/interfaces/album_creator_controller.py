from abc import ABC, abstractmethod


class AlbumCreatorControllerInterface(ABC):

    @abstractmethod
    def create_album(self, album_info: dict) -> dict:
        pass
