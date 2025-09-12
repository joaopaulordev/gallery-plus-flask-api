from .album_creator_controller import AlbumCreatorController
from src.models.sqlite.entities.album import AlbumTable

class MockPhotoRepository:
    def create_album(self, album: AlbumTable) -> None: pass

def test_create_album():
    album_infor = {
        "title": "Album Teste"
    }

    controller = AlbumCreatorController(MockPhotoRepository())
    response = controller.create_album(album_infor)
   
    assert response["id"] == None
    assert response["title"] == "Album Teste"

