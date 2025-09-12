from abc import ABC, abstractmethod


class PhotoFinderControllerInterface(ABC):

    @abstractmethod
    def find_photo_by_id(self, photo_id: int) -> dict:
        pass
