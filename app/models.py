from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    numberOfQuestions = db.Column(db.Integer)
    correct = db.Column(db.Integer)
    time = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % (self.nickname)