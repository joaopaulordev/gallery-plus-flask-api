from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.entities.photo import PhotoTable
from src.models.sqlite.entities.album import AlbumTable

# Assuming session is an active SQLAlchemy session
new_photo = PhotoTable(title="Title Photo 2", imageId="image photo 2")
new_album = AlbumTable(title="Title Album 3")
new_album2 = AlbumTable(title="Title Album 4")

# Add a album to a photo
new_photo.albums.append(new_album)
new_photo.albums.append(new_album2)


# db_connection_handler.connect_to_db()

with db_connection_handler as database:
    try:
        database.session.add(new_photo)
        database.session.commit()
    except Exception as exception:
        database.session.rollback()
        raise exception


# Accessing related objects
for album in new_photo.albums:
    print(f"Photo:{new_photo.title} - Album: {album.title}")

for photo in new_album.photos:
    print(f"Album:{new_album.title} - Photos:  {photo.title}")


