from app import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import date

class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True)
    creation_date = Column(Date)

    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'creation_date': self.creation_date.isoformat()
        }

    def __repr__(self):
        return "<Group(code - '%s', creation date - '%s')" % (
            self.code, self.creation_date)
