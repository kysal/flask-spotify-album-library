from . import db

class Album(db.Model):
    album_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512))
    added_at = db.Column(db.DateTime(timezone=True))


class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))


# class AlbumArtist(db.Model):
#     albums = db.relationship('Album')
#     artists = db.relationship('Artist')