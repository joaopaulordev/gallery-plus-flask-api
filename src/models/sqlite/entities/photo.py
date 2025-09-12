from sqlalchemy import Column, String, BIGINT, Table, ForeignKey
from src.models.sqlite.settings.base import Base, relationship

from .album import AlbumTable   #it is defined here because has to be load before PhotoTable


# Define the association table
photo_album_association = Table(
    'photo_album_association', Base.metadata,
    Column('photo_id', BIGINT, ForeignKey('photos.id')),
    Column('album_id', BIGINT, ForeignKey('albums.id'))
)

class PhotoTable(Base):
    __tablename__ = "photos"

    id = Column(BIGINT, primary_key=True)
    title = Column(String, nullable=False)
    imageId = Column(String, nullable=False)
    # Define the relationship to Album through the association table
    albums = relationship(
        'AlbumTable',
        secondary=photo_album_association,
        backref='photos' # Allows accessing photos from a Album object
    )

    def __repr__(self):
        return f"Photo [title={self.title}, imageId={self.imageId}]"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "albumsIds": [],
            "imageId": self.imageId,
            "albums": [album.to_dict() for album in self.albums]
        }


