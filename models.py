from app import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    room = db.Column(db.String(120), index=True, unique=False)
    week = db.Column(db.String(64), index=True, unique=False)

    def __init__(self, name, room, week):
    	self.name = name
    	self.room = room
    	self.week = week

    def __repr__(self):
        return '<Assignment %r>' % (self.name+self.room+self.week)
