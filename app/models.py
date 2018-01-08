from datetime import datetime as dt
from app import db

class List(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String(8), unique=True, index=True)
	tasks = db.relationship('Task', backref='list', lazy='dynamic')

	def __repr__(self):
		return '<link to list: %s>' % self.link

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime, index=True, default=dt.utcnow)
	list_id = db.Column(db.Integer, db.ForeignKey('list.id'))