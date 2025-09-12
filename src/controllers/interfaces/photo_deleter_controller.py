from abc import ABC, abstractmethod

class PhotoDeleterControllerInterface(ABC):

    @abstractmethod
    def delete_photo(self, photo_id: int) -> None:
        pass
