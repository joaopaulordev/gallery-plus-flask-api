from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.photo import PhotoTable
from src.models.sqlite.interfaces.photo_repository import PhotoRepositoryInterface

class PhotoRepository(PhotoRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_photo(self, photo: PhotoTable) -> None:
        with self.__db_connection as database:
            try:
                database.session.add(photo)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            

    def get_photo_by_id(self, photo_id: int) -> PhotoTable:
        with self.__db_connection as database:
            try:
                photo = database.session.query(PhotoTable).filter(PhotoTable.id == photo_id).first()  
                return photo
            except NoResultFound:
                return None
            

    def get_photos(self) -> list[PhotoTable]:
        with self.__db_connection as database:
            try:
                photos = database.session.query(PhotoTable).all()
                return photos
            except NoResultFound:
                return []
            
            
    def delete_photo(self, photo_id: int) -> None:
        with self.__db_connection as database:
            try:
                database.session.query(PhotoTable).filter(PhotoTable.id == photo_id).delete()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
