CREATE TABLE IF NOT EXISTS photos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    imageId TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);


CREATE TABLE photo_album_association (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	photo_id INTEGER NOT NULL,
	album_id INTEGER NOT NULL,
	CONSTRAINT photo_album_association_albums_FK FOREIGN KEY (album_id) REFERENCES albums(id),
	CONSTRAINT photo_album_association_photos_FK FOREIGN KEY (photo_id) REFERENCES photos(id)
);
