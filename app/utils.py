from app import db
from app.models import List
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
	
