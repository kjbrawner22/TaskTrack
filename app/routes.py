from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	title = "Task Track | Home"
	return render_template('index.html', title=title)

@app.route('/about')
def about():
	title = "Task Track | About"
	return render_template('about.html', title=title)

@app.route('/list/<id>')
def list(id):
	return render_template('index.html')