from .. import db

class Snack(db.Model):
    """
    Database model for our Snack class
    """
    __tablename__ = "snacks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    @staticmethod
    def generate_fake():
        names = ['ramen', 'lava cakes', 'margs', 'nachos']
        for name in names:
            db.session.add(Snack(name=name))
        db.session.commit()