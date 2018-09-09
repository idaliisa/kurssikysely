from application import db
from sqlalchemy.sql import text


class Question(db.Model):

    __tablename__ = "Kysymys"

    id = db.Column(db.Integer, primary_key=True)
    kysymys = db.Column(db.String(500), nullable=False)
    kysymystyyppi = db.Column(db.String(25), nullable=False)
    vastaukset = db.relationship("Answer", backref='Kysymys', lazy=True)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('Kayttaja.id'), nullable=False)

    def __init__(self, kysymys, kysymystyyppi):
        self.kysymys = kysymys
        self.kysymystyyppi = kysymystyyppi

    @staticmethod
    def etsi_kurssille_kysymykset():
        stmt = text("SELECT kysymys FROM 'Kysymys'")
        res = db.engine.execute(stmt)

        kysymykset = []

        for row in res:
            kysymykset.append(row)

        return kysymykset