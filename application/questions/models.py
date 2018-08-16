from application import db

class Question(db.Model):

    __tablename__ = "Kysymys"

    id = db.Column(db.Integer, primary_key=True)
    kysymys = db.Column(db.String(500), nullable=False)
    kysymystyyppi = db.Column(db.String(25), nullable=False)

    vastaukset = db.relationship("Answer", backref='Kysymys', lazy=True)

    def __init__(self, kysymys, kysymystyyppi):
        self.kysymys = kysymys
        self.kysymystyyppi = kysymystyyppi