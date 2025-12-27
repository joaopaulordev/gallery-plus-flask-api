from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base


class AlbumTable(Base):
    __tablename__ = "albums"

    id = Column(BIGINT, primary_key=True)
    title = Column(String, nullable=False)

    def __repr__(self):
        return f"Album [title={self.title}]"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }


