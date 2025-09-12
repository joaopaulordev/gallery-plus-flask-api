from src.models.sqlite.entities.photo import PhotoTable
from .photo_lister_controller import PhotoListerController
from src.models.sqlite.entities.photo import PhotoTable
from src.models.sqlite.entities.album import AlbumTable


class MockPhotosRepository:
    def get_photos(self) -> list[PhotoTable]:
        new_photo = PhotoTable(title="Title Photo 1", imageId="image photo 1")
        new_album = AlbumTable(title="Title Album 1")
        new_album2 = AlbumTable(title="Title Album 2")

        new_photo.albums.append(new_album)
        new_photo.albums.append(new_album2)

        return [new_photo]

def test_list_photos():
    controller = PhotoListerController(MockPhotosRepository())
    response = controller.list_photos()

    expected_response = [
        {
            'id': None, 
            'title': 'Title Photo 1', 
            'albumsIds': [], 
            'imageId': 'image photo 1', 
            'albums': [
                {
                    'id': None, 
                    'title': 'Title Album 1'
                }, 
                {
                    'id': None, 
                    'title': 'Title Album 2'
                }
            ]
        }
    ]


    assert response == expected_response