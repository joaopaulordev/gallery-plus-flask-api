from src.models.sqlite.entities.album import AlbumTable
from .album_lister_controller import AlbumListerController



class MockAlbumsRepository:
    def get_albums(self) -> list[AlbumTable]:   
        new_album = AlbumTable(title="Title Album 1")
        new_album2 = AlbumTable(title="Title Album 2")

        return [new_album, new_album2]

def test_list_albums():
    controller = AlbumListerController(MockAlbumsRepository())
    response = controller.list_albums()

    expected_response = [
        {
            'id': None, 
            'title': 'Title Album 1' 
        },
        {
            'id': None, 
            'title': 'Title Album 2' 
        }
    ]


    assert response == expected_response