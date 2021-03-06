from app.main import db
from app.main.models.teacher import Teacher
from flask import jsonify

def get_all_teachers():
    """[summary]
    
    Returns:
        [type]: [description]
    """
    
    query = db.session.query(Teacher).all()
    items = []
    for i in query:
        items.append({"teacher_id":i.Teacher.teacher_id,"teacher_name":i.Teacher.teacher_name})
    response_object = jsonify({"data":items})
    return response_object, 200