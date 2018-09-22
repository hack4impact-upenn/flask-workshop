### Newbie database model ###

from .. import db

class Newbie(db.Model):
    __tablename__ = "newbies"

    # Primary keys differentiate between unique entries in the database
    id = db.Column(db.Integer, primary_key=True)
    # Columns are properties/attributes
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    year = db.Column(db.Integer)
