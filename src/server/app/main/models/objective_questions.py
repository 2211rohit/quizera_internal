from .. import db

class ObjectiveQuestions(db.Model):
    __tablename__ = 'objective_questions'
    """[Create Objective Questions Table]
    """
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Text, nullable=False)
    option_1 = db.Column(db.Text,nullable=True)
    option_2 = db.Column(db.Text,nullable=True)
    option_3 = db.Column(db.Text,nullable=True)
    option_4 = db.Column(db.Text,nullable=True)
    answer = db.Column(db.Text,nullable=False)
    marks = db.Column(db.Integer,nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.teacher_id'),nullable=False)
    quiz_test_id = db.Column(db.Integer,db.ForeignKey('quiztest.test_id'),nullable=False)
    objective_type_id = db.Column(db.Integer,db.ForeignKey('objective_type.objective_type_id'),nullable=False)
    teachers = db.relationship('Teacher',backref=db.backref('objective_questions', lazy=True))
    quizset = db.relationship('Quizset',backref=db.backref('objective_questions', lazy=True))
    objective_type = db.relationship('ObjectiveType',backref=db.backref('objective_questions', lazy=True))