from .photo_finder_controller import PhotoFinderController
from src.models.sqlite.entities.photo import PhotoTable

class MockPhotoRepository:
    def get_photo_by_id(self, photo_id: int) -> PhotoTable:
        new_photo = PhotoTable(title="Photo Teste", imageId="image-teste.jpg")
        return new_photo

def test_find_photo_by_id():    
    controller = PhotoFinderController(MockPhotoRepository())
    response = controller.find_photo_by_id(3)
   
    expected_response = {
        'id': None, 
        'title': 'Photo Teste', 
        'albumsIds': [], 
        'imageId': 'image-teste.jpg', 
        'albums': [], 
        'nextPhotoId': 11, 
        'previousPhotoId': 0
    }

    assert response == expected_response
