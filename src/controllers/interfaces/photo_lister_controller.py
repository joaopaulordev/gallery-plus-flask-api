from abc import ABC, abstractmethod

class PhotoListerControllerInterface(ABC):

    @abstractmethod
    def list_photos(self) -> dict:
        pass
