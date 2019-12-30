from .. import db


class Teacher(db.Model):
    __tablename__ = 'teacher'
    """[Create Teacher Table]
    """
    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_name = db.Column(db.String(250), nullable=False)