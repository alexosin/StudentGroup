from app import db
from app.models import Group
import datetime

g = Group(code='IK-21', creation_date=datetime.date(2013, 6, 30))
db.session.add(g)
db.session.commit()
