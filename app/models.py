from app import db

class List(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String(8), unique=True, index=True)

	def __repr__(self):
		return '<link to list: %s>' % self.link