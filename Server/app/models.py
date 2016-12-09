from app import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from datetime import date
from sqlalchemy.orm import relationship, backref

class Person(db.Model):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    surname = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    patronymic = Column(String(30))
    birth_date = Column(Date)
    sex = Column(Integer)
    birth_place = Column(String(40))
    address = Column(String(40))
    telephone = Column(String(20))
    violation = relationship('Violation', backref='persons')
    student = relationship('Student', backref=backref('persons', uselist=False))

    def serialize(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'name': self.name,
            'patronymic': self.patronymic,
            'birth_date': self.patronymic,
            'sex': self.sex,
            'birth_place': self.birth_place,
            'address': self.address,
            'telephone': self.telephone
        }

    def __repr__(self):
        return "<Person(surname %s, name %s, patronymic %s)" % (
            self.name, self.surname, self.patronymic
        )

class Student(db.Model):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    book_number = Column(String(15), unique=True)
    note = Column(String(46))
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('Person', backref=backref('students', uselist=False))
    student_group = relationship('StudentGroup', backref='student')
    student_marks = relationship('StudentMark', backref='student')
    contract = relationship('Contract', backref='student')

    def serialize(self):
        return {
            'id': self.id,
            'book_number': self.book_number,
            'note': self.note,
            'person_id': self.person_id
        }

    def __repr__(self):
        return "<Student(book_number %s, note %s)" % (
            self.book_number, self.note
        )

class OrderKind(db.Model):
    __tablename__ = 'order_kind'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    order_kind = relationship('Order', backref="order_kind")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return "<OrderKind(name - '%s')" % (self.name)

class PunishKind(db.Model):
    __tablename__ = 'punish_kind'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    violation = relationship('Violation', backref='punish_kind')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return "<PunishKind(name - '%s')" % (self.name)

class ViolationKind(db.Model):
    __tablename__ = 'violation_kind'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    violation = relationship('Violation', backref='violation_kinds')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return "<ViolationKind(name - '%s')" % (self.name)

class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True)
    creation_date = Column(Date)
    student_group = relationship('StudentGroup', backref='group')

    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'creation_date': self.creation_date.isoformat()
        }

    def __repr__(self):
        return "<Group(code - '%s', creation date - '%s')>" % (
            self.code, self.creation_date)

class Mark(db.Model):
    __tablename__  = 'mark'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    student_marks = relationship('StudentMark', backref='mark')

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }

    def __repr__(self):
        return "<Mark(name - '%s')>" % (self.name)

class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    number = Column(Integer, unique=True)
    text = Column(String)
    order_kind_id = Column(Integer, ForeignKey('order_kind.id'))
    violation = relationship('Violation', backref='orders')

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'text': self.text,
            'order_kind': self.order_kind_id
        }

    def __repr__(self):
        return "<Order(date - %s, number - %s, text - %s)" % (
            self.date, self.number, self.text
        )

class Violation(db.Model):
    __tablename__ = 'violation'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    violation_kind = Column(Integer, ForeignKey('violation_kind.id'))
    punish_kind_id = Column(Integer, ForeignKey('punish_kind.id'))
    person_id = Column(Integer, ForeignKey('persons.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))

    def serialize(self):
        return {
        'id': self.id,
        'date': self.date,
        'violation_kind': self.violation_kind,
        'punish_kind': self.punish_kind_id,
        'person': self.person_id,
        'order': self.order_id
    }

    def __repr__(self):
        return "<Violation(date - %s" % (self.date)

class StudentGroup(db.Model):
    __tablename__ = 'student_groups'

    id = Column(Integer, primary_key=True)
    putting_date = Column(Date)
    student_id = Column(Integer, ForeignKey('students.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

    def serialize(self):
        return {
        'id': self.id,
        'putting_date': self.putting_date,
        'student_id': self.student_id,
        'group_id': self.group_id
        }

    def __repr__(self):
        return "<StudentGroup(putting date - %s)" % (self.putting_date)

class StudentMark(db.Model):
    __tablename__ = 'student_marks'

    id = Column(Integer, primary_key=True)
    mark_id = Column(Integer, ForeignKey('mark.id'))
    student_id = Column(Integer, ForeignKey('students.id'))

    def serialize(self):
        return {
        'id': self.id,
        'mark_id': self.mark_id,
        'student_id': self.student_id
    }

    def __repr__(self):
        return "<StudentMark(id - %s)" % (
            self.id
        )

class ContractKind(db.Model):
    __tablename__ = 'contract_kind'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    contract = relationship('Contract', backref='contract_kind')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return "<OrderKind(name - '%s')" % (self.name)

class Contract(db.Model):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    number = Column(Integer, unique=True)
    total_sum = Column(Float(precision=2))
    payer_kind = Column(String)
    contract_kind_id = Column(Integer, ForeignKey('contract_kind.id'))
    student_id = Column(Integer, ForeignKey('students.id'))

    def serialize(self):
        return {
        'id': self.id,
        'date': self.date,
        'number': self.number,
        'payer_kind': self.payer_kind,
        'self.contract_kind_id': self.contract_kind_id,
        'student_id': self.student_id
    }

    def __repr__(self):
        return "<Contract(date - %s, number - %s, total sum - %s, payer - %s)" % (
            self.date, self.number, self.total_sum, self.payer_kind
        )

