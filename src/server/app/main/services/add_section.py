from app.main import db
from app.main.models.section import Section
from flask import jsonify


def add_new_section(data):
    section = Section(
        section_name = data['section_name'],
        batch_id = data['batch_id']
    )
    db.session.add(section)
    db.session.commit()
    response_object = jsonify({"response": "successfully added Batch"})
    return response_object, 200
