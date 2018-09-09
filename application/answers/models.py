from application import db

class Answer(db.Model):

    __tablename__ = "Vastaus"

    id = db.Column(db.Integer, primary_key=True)
    vastaus = db.Column(db.String(500), nullable=False)    
    kysymys_id = db.Column(db.Integer, db.ForeignKey('Kysymys.id'), nullable=False)

    def __init__(self, vastaus):
        self.vastaus = vastaus