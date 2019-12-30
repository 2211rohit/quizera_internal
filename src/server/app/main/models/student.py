from .. import db


class Student(db.Model):
    __tablename__ = 'student'
    """[Create Student Table]
    """
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_name = db.Column(db.String(250), nullable=False)