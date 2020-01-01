from .. import db


class Teacher(db.Model):
    """[summary]   
    Args:
        db ([type]): [description]
    """
    __tablename__ = 'teacher'
    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_name = db.Column(db.String(250), nullable=False)