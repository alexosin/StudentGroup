from app import app
from flask import jsonify
from .models import Group


@app.route('/groups', methods=['GET'])
def get_tasks():
    groups = Group.query.all()
    return jsonify({'groups': [g.serialize() for g in groups]})
