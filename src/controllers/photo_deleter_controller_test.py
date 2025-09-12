from src.controllers.photo_deleter_controller import PhotoDeleterController

def test_delete_photo(mocker):
    mock_repository = mocker.Mock()
    controller = PhotoDeleterController(mock_repository)
    controller.delete_photo(3)

    mock_repository.delete_photo.assert_called_once_with(3)
