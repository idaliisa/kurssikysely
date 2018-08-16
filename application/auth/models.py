from application import db

class User(db.Model):

    __tablename__ = "Kayttaja"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(150), nullable=False)
    kayttajatunnus = db.Column(db.String(150), nullable=False)
    salasana = db.Column(db.String(150), nullable=False)
    kayttajatyyppi = db.Column(db.String(150), nullable=False)

    def __init__(self, nimi, kayttajatunnus, salasana, kayttajatyyppi):
        self.nimi = nimi
        self.salasana = salasana
        self.kayttajatunnus = kayttajatunnus
        self.kayttajatyyppi = kayttajatyyppi

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


