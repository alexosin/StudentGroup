from app import app, db
from flask import jsonify
import json
from .models import *

@app.route('/groups', methods=['GET'])
def get_tasks():
    groups = Group.query.all()
    return json.dumps({'groups': [g.serialize() for g in groups]})

@app.route('/students/<int:group_id>', methods=['GET'])
def get_students(group_id):
    q = db.session.query(StudentGroup, Student, Person). \
        filter(group_id==StudentGroup.group_id). \
        filter(StudentGroup.student_id==Student.id). \
        filter(Student.person_id==Person.id).all()
    students = []
    persons = []
    for (group, student, person) in q:
         students.append(student.serialize())
         persons.append(person.serialize())
    return json.dumps({'students': students, 'persons': persons})
