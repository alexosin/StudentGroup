from app import app
from flask import jsonify
import json
from .models import Group


@app.route('/groups', methods=['GET'])
def get_tasks():
    groups = Group.query.all()
    return json.dumps({'groups': [g.serialize() for g in groups]})
