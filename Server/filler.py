from app import db
import app.models as model
import datetime

db.session.add_all([
    # violationkind
    model.ViolationKind(name='violation_first'),
    model.ViolationKind(name='violation_second'),
    model.ViolationKind(name='violation_third'),
    #punishkind
    model.PunishKind(name='punish_first'),
    model.PunishKind(name='punish_second'),
    model.PunishKind(name='punish_third'),
    #orderkind
    model.OrderKind(name='order_first'),
    model.OrderKind(name='order_second'),
    model.OrderKind(name='order_third'),
    #orders
    model.Order(
        date=datetime.date(2013, 7, 30),
        number=1,
        order_kind_id=1
        ),
    #groups
    model.Group(code='IK-22', creation_date=datetime.date(2013, 6, 30)),
    model.Group(code='IK-23', creation_date=datetime.date(2012, 4, 5)),
    model.Group(code='Ik-33', creation_date=datetime.date(2012, 12, 12)),
    #marks
    model.Mark(name='A'),
    model.Mark(name='B'),
    model.Mark(name='C'),
    model.Mark(name='D'),
    model.Mark(name='E'),
    #persons
    model.Person(surname='Osin', name='Alexander', sex=1),
    model.Person(surname='Jordan', name='Mike', sex=1),
    model.Person(surname='Lox', name='Anya', sex=2),
    #students
    model.Student(book_number='IK3349', person_id=1),
    model.Student(book_number='IK3348', person_id=2),
    model.Student(book_number='Ik3347', person_id=3),
    #studentMarks
    model.StudentMark(mark_id=1, student_id=1),
    model.StudentMark(mark_id=1, student_id=2),
    model.StudentMark(mark_id=2, student_id=1),
    #studentGroups
    model.StudentGroup(
        putting_date=datetime.date(2013, 12, 12), 
        group_id=1,
        student_id=1),
    model.StudentGroup(
        putting_date=datetime.date(2013, 12, 12), 
        group_id=1,
        student_id=2),
    model.StudentGroup(
        putting_date=datetime.date(2013, 12, 12), 
        group_id=1,
        student_id=3),
    #violations
    model.Violation(
        date=datetime.date(2013, 12, 12),
        violation_kind=1,
        punish_kind_id=1,
        person_id=1,
        order_id=1
        ),
    #contractKind
    model.ContractKind(name='contract_first'),
    model.ContractKind(name='contract_second'),
    #contracts
    model.Contract(
        date=datetime.date(2013, 12, 12),
        number=12,
        total_sum=60000,
        student_id=1,
        contract_kind_id=1
    )
])

db.session.commit()

