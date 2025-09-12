from src.controllers.album_deleter_controller import AlbumDeleterController

def test_delete_album(mocker):
    mock_repository = mocker.Mock()
    controller = AlbumDeleterController(mock_repository)
    controller.delete_album(3)

    mock_repository.delete_album.assert_called_once_with(3)
