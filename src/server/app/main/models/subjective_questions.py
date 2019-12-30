from .. import db

class SubjectiveQuestions(db.Model):
    __tablename__ = 'subjective_questions'
    """[Create Subjective Questions Table]
    """
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text,nullable=False)
    marks = db.Column(db.Integer,nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.teacher_id'),nullable=False)
    quiz_test_id = db.Column(db.Integer,db.ForeignKey('quizset.test_id'),nullable=False)
    teachers = db.relationship('Teacher',backref=db.backref('objective_questions', lazy=True))
    quizset = db.relationship('Quizset',backref=db.backref('objective_questions', lazy=True))