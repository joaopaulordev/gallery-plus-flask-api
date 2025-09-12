from abc import ABC, abstractmethod


class PhotoCreatorControllerInterface(ABC):

    @abstractmethod
    def create_photo(self, photo_info: dict) -> dict:
        pass
