from application import db
from application.auth import models
from sqlalchemy.sql import text

KurssiKayttaja = db.Table('KurssiKayttaja',
    db.Column('kurssi_id', db.Integer, db.ForeignKey('Kurssi.id'), primary_key=True),
    db.Column('kayttaja_id', db.Integer, db.ForeignKey('Kayttaja.id'), primary_key=True)
)

class Course(db.Model):

    __tablename__ = "Kurssi"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(500), nullable=False)
    laitos = db.Column(db.String(50), nullable=False)
    tiedekunta = db.Column(db.String(50), nullable=False)
    kayttajat = db.relationship('User', secondary=KurssiKayttaja, backref='kurssi')
   
    def __init__(self, nimi, laitos, tiedekunta):
        self.nimi = nimi
        self.laitos = laitos
        self.tiedekunta = tiedekunta

    def poista_KurssiKayttaja(kurssi_id):
        stmt = KurssiKayttaja.delete(kurssi_id=kurssi_id)
        db.session.execute(stmt)
        db.session.commit()
    
