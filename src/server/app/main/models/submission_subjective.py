from .. import db
import datetime

class SubmissionSubjective(db.Model):
    __tablename__ = 'submission_objective'
    """[Create Submission Objective Table]
    """
    submission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.question_id'),nullable=False)    
    question_id = db.Column(db.Integer,db.ForeignKey('subjective_questions.question_id'),nullable=False)
    response = db.Column(db.Text,default=None, nullable=True)
    marks = db.Column(db.Integer,default=None)
    quiz_test_id = db.Column(db.Integer,db.ForeignKey('quiztest.test_id'),nullable=False)
    submission_time = db.Column(db.DateTime,onupdate=datetime.datetime.now())
    question = db.relationship('SubjectiveQuestions',backref=db.backref('submission_objective', lazy=True))
    teachers = db.relationship('Teacher',backref=db.backref('submission_objective', lazy=True))
    quizset = db.relationship('Quizset',backref=db.backref('submission_objective', lazy=True))
