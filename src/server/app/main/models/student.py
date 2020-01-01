from .. import db


class Student(db.Model):
    """[summary]  
    Args:
        db ([type]): [description]
    """
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_name = db.Column(db.String(250), nullable=False)