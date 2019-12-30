from app.main import db
from app.main.models.section import Section
from flask import jsonify


def delete_section(data):
    section = Section.query.get(int(data["section_id"]))
    db.session.delete(section)
    db.session.commit()
    response_object = jsonify({"response": "successfully deleted"})
    return response_object, 200