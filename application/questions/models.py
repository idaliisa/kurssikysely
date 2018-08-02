from application import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kysymys = db.Column(db.String(500), nullable=False)
    kysymystyyppi = db.Column(db.String(25), nullable=False)

    def __init__(self, kysymys, kysymystyyppi):
        self.kysymys = kysymys
        self.kysymystyyppi = kysymystyyppi