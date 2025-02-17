from app import db

class IICS(db.Model):
    __tablename__ = 'iics'

    id = db.Column(db.Integer, primary_key=True)
    infants = db.Column(db.String)
    diplomats = db.Column(db.String)
    deportees = db.Column(db.String)

    def __repr__(self):
        return f'IICS with {self.infants}, {self.diplomats} and {self.deportees}'


class GIA(db.Model):
    __tablename__ = 'gia'

    id = db.Column(db.Integer, primary_key=True)
    infants = db.Column(db.String)
    diplomats = db.Column(db.String)
    deportees = db.Column(db.String)

    def __repr__(self):
        return f'GIA with {self.infants}, {self.diplomats} and {self.deportees}'


