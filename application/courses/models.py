from application import db

class Course(db.Model):

    __tablename__ = "Kurssi"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(500), nullable=False)
    laitos = db.Column(db.String(50), nullable=False)
    tiedekunta = db.Column(db.String(50), nullable=False)

    def __init__(self, nimi, laitos, tiedekunta):
        self.nimi = nimi
        self.laitos = laitos
        self.tiedekunta = tiedekunta