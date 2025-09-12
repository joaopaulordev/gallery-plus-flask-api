from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.album import AlbumTable
from src.models.sqlite.interfaces.album_repository import AlbumRepositoryInterface

class AlbumRepository(AlbumRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_album(self, album: AlbumTable) -> None:
        with self.__db_connection as database:
            try:
                database.session.add(album)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            

    def get_album_by_id(self, album_id: int) -> AlbumTable:
        with self.__db_connection as database:
            try:
                album = database.session.query(AlbumTable).filter(AlbumTable.id == album_id).first()  
                return album
            except NoResultFound:
                return None
            

    def get_albums(self) -> list[AlbumTable]:
        with self.__db_connection as database:
            try:
                albums = database.session.query(AlbumTable).all()
                return albums
            except NoResultFound:
                return []
            
            
    def delete_album(self, album_id: int) -> None:
        with self.__db_connection as database:
            try:
                database.session.query(AlbumTable).filter(AlbumTable.id == album_id).delete()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
