from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime as dt
from app import db

class List(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String(8), unique=True, index=True)
	pin_hash = db.Column(db.String(128), default='placeholder_hash')
	tasks = db.relationship('Task', backref='list', lazy='dynamic')

	def set_pin_hash(self, pin):
		self.pin_hash = generate_password_hash(pin)

	def check_pin_hash(self, pin):
		return check_password_hash(self.pin_hash, pin)

	def __repr__(self):
		return '<Link to list: %s>' % self.link

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(64), default="A task")
	timestamp = db.Column(db.DateTime, index=True, default=dt.utcnow)
	do_by = db.Column(db.DateTime, index=True, default=dt.utcnow)
	priority = db.Column(db.String(6), default='Low')
	list_id = db.Column(db.Integer, db.ForeignKey('list.id'))

	def __repr__(self):
		return '<Task: %s>' % self.text