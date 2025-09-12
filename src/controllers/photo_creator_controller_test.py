from .photo_creator_controller import PhotoCreatorController
from src.models.sqlite.entities.photo import PhotoTable

class MockPhotoRepository:
    def create_photo(self, photo: PhotoTable) -> None: pass

def test_create_photo():
    photo_infor = {
        "title": "Foto Teste"
    }

    controller = PhotoCreatorController(MockPhotoRepository())
    response = controller.create_photo(photo_infor)

    assert response["title"] == "Foto Teste"
    assert response["albumsIds"] == []

