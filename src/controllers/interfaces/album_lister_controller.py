from abc import ABC, abstractmethod

class AlbumListerControllerInterface(ABC):

    @abstractmethod
    def list_albums(self) -> dict:
        pass
