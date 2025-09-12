from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.entities.photo import PhotoTable
from src.models.sqlite.entities.album import AlbumTable

# db_connection_handler.connect_to_db()

with db_connection_handler as database:
    try:
        photo_db = database.session.query(PhotoTable).filter(PhotoTable.id == 4).one()
        # Accessing related objects
        for album in photo_db.albums:
            print(f"Photo:{photo_db.title} - Album: {album.title}")

        album_db = database.session.query(AlbumTable).filter(AlbumTable.id == 5).one()
        for photo in album_db.photos:
            print(f"Album:{album_db.title} - Photos:  {photo.title}")
    except Exception as exception:
        database.session.rollback()
        raise exception

