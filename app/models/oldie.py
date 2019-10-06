from .. import db

class Oldie(db.Model):
    """
    Database model for our Oldie class
    """
    __tablename__ = "oldies"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    year = db.Column(db.Integer)
    # This defines a one-to-many relationship with the Newbie class!
    mentees = db.relationship('Newbie', backref='mentor')

    @staticmethod
    def generate_fake():
        katie = Oldie(
            first_name='Katie',
            last_name='Jiang',
            year=2020)
        steph = Oldie(
            first_name='Stephanie',
            last_name='Shi',
            year=2020)

        db.session.add(katie)
        db.session.add(steph)
        db.session.commit()