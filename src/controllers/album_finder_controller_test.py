from .album_finder_controller import AlbumFinderController
from src.models.sqlite.entities.album import AlbumTable

class MockAlbumRepository:    
    def get_album_by_id(self, album_id: int) -> AlbumTable:
        album = AlbumTable(title="Photo Teste", id=2)
        return album

def test_find_photo_by_id():    
    controller = AlbumFinderController(MockAlbumRepository())
    response = controller.find_album_by_id(2)
   
    expected_response = {
        "id": 2,
        "title": "Photo Teste"
    }

    assert response == expected_response
