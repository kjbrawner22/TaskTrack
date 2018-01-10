from app import db
from app.models import List,Task
import string
from random import choice

def new_list_link(links):
	allchars = string.ascii_letters + string.digits
	link = "".join(choice(allchars) for x in range(8))
	while link in links:
		link = "".join(choice(allchars) for x in range(8))	
	l = List(link=link)
	db.session.add(l)
	db.session.commit()
	return link

def list_exists(link):
	lists = List.query.filter_by(link=link).first()
	if lists is not None:
		return True
	else:
		return False

def get_list_by_link(link):
	l = List.query.filter_by(link=link).first()
	if l is not None:
		return l.id
	else:
		return None

def add_task(text, do_by, priority, list_id):
	t = Task(text=text, do_by=do_by,
		       priority=priority, list_id=list_id)
	db.session.add(t)
	db.session.commit()
	
