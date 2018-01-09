#!venv/bin/python3

from app import app,db
from app.models import List,Task

@app.shell_context_processor
def make_shell_context():
	return {
		'db' : db,
		'List' : List,
		'Task' : Task
	}

app.run(debug=True)