from utils.sqlalchemy import db

class Dream(db.Model):

    __tablename__ = 'dreams'

    id = db.Column(db.Integer, primary_key=True)
    dream = db.Column(db.String)
    completed = db.Column(db.Boolean)

    def to_json(self):
        return {
                   "id": self.id,
                   "dream": self.dream,
                   "completed": self.completed
               }

    def from_json(self, source):
        if 'dream' in source:
            self.dream = source['dream']
        if 'completed' in source:
            self.completed = source['completed']
