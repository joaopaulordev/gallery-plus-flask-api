from abc import ABC, abstractmethod

class AlbumDeleterControllerInterface(ABC):

    @abstractmethod
    def delete_album(self, album_id: int) -> None:
        pass
