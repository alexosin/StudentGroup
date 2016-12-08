from app import db
import app.models as model
import datetime

db.session.add_all([
    model.ViolationKind(name='violation_first'),
    model.ViolationKind(name='violation_second')
])

db.session.add_all([
    model.PunishKind(name='punish_first'),
    model.PunishKind(name='punish_second')
])

db.session.add_all([
    model.OrderKind(name='order_first'),
    model.OrderKind(name='order_second')
])

db.session.add_all([
    model.Group(code='IK-22', creation_date=datetime.date(2013, 6, 30)),
    model.Group(code='IK-23', creation_date=datetime.date(2012, 4, 5))
])

db.session.add_all([
    model.StudentGroup(
        group_id=1, 
        putting_date=datetime.date(2013, 12, 12),
        student_id=1
        ),
    model.StudentGroup(
        group_id=2, 
        putting_date=datetime.date(2013, 1, 14),
        student_id=2
        )
])

db.session.add_all([
    model.Person(
        surname='Osin',
        name='Alexander',
        sex=0
    )
])

db.session.add_all([
    model.Student(book_number='IK3349', person_id=1),
    model.Student(book_number='IK3348', person_id=1)
])

db.session.commit()

