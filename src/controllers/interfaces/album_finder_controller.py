from abc import ABC, abstractmethod


class AlbumFinderControllerInterface(ABC):

    @abstractmethod
    def find_album_by_id(self, album_id: int) -> dict:
        pass
