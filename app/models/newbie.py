from .. import db

class Newbie(db.Model):
    """
    Database model for our Newbie class
    """
    # Allows us to specify the name of our table. If we don't add this line,
    # SQLAlchemy automatically generates the table name from our class name.
    __tablename__ = "newbies"

    # Primary keys differentiate between unique entries in the database
    # This is automatically generated for us. Thanks SQLAlchemy!
    id = db.Column(db.Integer, primary_key=True)
    # Columns are properties/attributes
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    year = db.Column(db.Integer)
    # This defines a one-to-many relationship with the Oldie class
    mentor_id = db.Column(db.Integer, db.ForeignKey('oldies.id'), nullable=True)

    @staticmethod
    def generate_fake():
        christina = Newbie(
            first_name='Christina',
            last_name='Lu',
            year=2022
        )
        lisa = Newbie(
            first_name='Lisa',
            last_name='Moshiro',
            year=2022
        )
        robin = Newbie(
            first_name='Robin',
            last_name='Tan',
            year=2022
        )
        
        for newbie in [christina, lisa, robin]:
            db.session.add(newbie)
        db.session.commit()