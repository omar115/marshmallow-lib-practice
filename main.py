from datetime import date, datetime
from pprint import pprint
from marshmallow import Schema, fields, schema

class ArtistSchema(Schema):
    name = fields.Str()

class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

bowie = dict(name="David Bowie")
album = dict(artist=bowie, title="Hunky Dory", release_date=date(2020, 12, 12))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result, indent=4)