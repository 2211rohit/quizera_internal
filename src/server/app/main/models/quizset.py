from .. import db

class Quizset(db.Model):
    """[summary]    
    Args:
        db ([type]): [description]
    """
    __tablename__ = 'quizset'
    test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test_name = db.Column(db.String(250), unique=True, nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.teacher_id'),nullable=False)
    time_full_test = db.Column(db.String(250), nullable=False)
    test_type_id = db.Column(db.Integer, db.ForeignKey('test_type.type_id'),nullable=False)
    student_section_id = db.Column(db.Integer,db.ForeignKey('section.section_id'),default = None,nullable=True)
    student_batch_id = db.Column(db.Integer,db.ForeignKey('batch.batch_id'),nullable=False)
    flag_publish_test = db.Column(db.Integer,default = 0,nullable = True)
    flag_jumble_question = db.Column(db.Integer, nullable=False)
    # test_open = db.Column(db.Integer,default = 1, nullable=True)
    teachers = db.relationship('Teacher',backref=db.backref('quizset', lazy=True))
    batches = db.relationship('Batch',backref=db.backref('quizset', lazy=True))
    test_types = db.relationship('TestType',backref=db.backref('quizset', lazy=True))
    sections = db.relationship('Section',backref=db.backref('quizset', lazy=True))
