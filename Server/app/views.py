from app import app, db
from flask import jsonify
import json
from .models import *
from sqlalchemy.sql import func

MARKS = {'A': 5, 'B': 4.5, 'C': 4, 'D': 3.5, 'E': 3}

@app.route('/groups', methods=['GET'])
def get_tasks():
    groups = Group.query.all()
    return json.dumps({'groups': [g.serialize() for g in groups]})

@app.route('/students/<int:group_id>', methods=['GET'])
def get_students(group_id):
    q = db.session.query(Student, Person). \
        filter(group_id==StudentGroup.group_id). \
        filter(StudentGroup.student_id==Student.id). \
        filter(Student.person_id==Person.id).all()
    students = []
    persons = []
    for (student, person) in q:
         students.append(student.serialize())
         persons.append(person.serialize())
    return json.dumps({'students': students, 'persons': persons})

@app.route('/contract/<int:person_id>', methods=['GET'])
def get_contract_for_person(person_id):
    q = db.session.query(Student, Contract, ContractKind). \
        filter(Person.id==person_id). \
        filter(person_id==Student.person_id). \
        filter(Student.id==Contract.student_id). \
        filter(Contract.contract_kind_id==ContractKind.id).first()
    contract = {}
    contract['date'] = q[1].date.isoformat()
    contract['book_number'] = q[0].book_number
    contract['kind'] = q[2].name
    contract['number'] = q[1].number
    contract['sum'] = q[1].total_sum
    return json.dumps({'contract': contract})

@app.route('/marks/<int:person_id>', methods=['GET'])
def get_marks_for_person(person_id):
    q = db.session.query(Mark). \
        filter(Person.id==person_id). \
        filter(person_id==Student.person_id). \
        filter(Student.id==StudentMark.student_id). \
        filter(StudentMark.mark_id==Mark.id).all()
    marks = []
    for i in q:
        marks.append(MARKS[i.name])
    return json.dumps({'marks': marks})

@app.route('/violations/<int:person_id>', methods=['GET'])
def get_violations_for_person(person_id):
    q = db.session.query(Violation, ViolationKind, Order, 
        OrderKind, PunishKind). \
        filter(Person.id==person_id). \
        filter(person_id==Student.person_id). \
        filter(Person.id==Violation.person_id). \
        filter(Violation.violation_kind==ViolationKind.id). \
        filter(Violation.punish_kind_id==PunishKind.id). \
        filter(Violation.order_id==Order.id). \
        filter(Order.order_kind_id==OrderKind.id).all()
    violation = set()
    for (viol, violk, order, ork, punk) in q:
        violation.add((viol, violk, order, ork, punk))
    violations = []
    for i in violation:
        v = {}
        v['date'] = i[0].date.isoformat()
        v['violation_kind'] = i[1].name
        v['order_date'] = i[2].date.isoformat()
        v['order_text'] = i[2].text
        v['order_number'] = i[2].number
        v['order_kind'] = i[3].name
        v['punish_kind'] = i[4].name
        violations.append(v)
    
    return json.dumps({'violations': violations})

@app.route('/query/<string:text>', methods=['GET'])
def get_query(text):
    QUERY_WORD = ['@third', '@second', '@first']
    if text not in QUERY_WORD:
        return json.dumps('Error')
    elif text == '@third':
        q = db.session.query(Person, Student, Contract, ContractKind). \
            filter(Person.id==Student.person_id). \
            filter(Student.id==Contract.student_id). \
            filter(Contract.contract_kind_id==ContractKind.id).\
            filter(ContractKind.name=='paid').all()
        persons = []
        for i in q:
            persons.append(i[0].serialize())
    elif text == '@second':
        q = db.session.query(Person). \
            filter(Student.person_id==Person.id).\
            filter(Person.id==Violation.person_id).\
            filter(Violation.punish_kind_id==PunishKind.id). \
            filter(PunishKind.name=='academic disqualification').all()
        persons = []
        for i in q:
            persons.append(i.serialize())            
    elif text == '@first':
        q = db.session.query(Person, Mark). \
            filter(Person.id==Student.person_id).\
            filter(Student.id==StudentMark.student_id).\
            filter(StudentMark.mark_id==Mark.id).all()
        checker = []
        for (person, mark) in q:
            if  mark.name != 'A':
                checker.append(person)
        persons = []
        for i in q:
            if i[0] not in checker:
                persons.append(i[0].serialize())
    return json.dumps({'persons': persons})
