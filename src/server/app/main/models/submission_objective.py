from .. import db
import datetime

class SubmissionObjective(db.Model):
    __tablename__ = 'submission_objective'
    """[Create Submission Objective Table]
    """
    submission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.student_id'),nullable=False)    
    question_id = db.Column(db.Integer,db.ForeignKey('objective_questions.question_id'),nullable=False)
    response = db.Column(db.Text,default=None, nullable=True)
    marks = db.Column(db.Integer,nullable=False)
    submission_time = db.Column(db.DateTime,onupdate=datetime.datetime.now())
    quiz_test_id = db.Column(db.Integer,db.ForeignKey('quizset.test_id'),nullable=False)
    students = db.relationship('Student',backref=db.backref('objective_question', lazy=True))
    quizset = db.relationship('Quizset',backref=db.backref('objective_question', lazy=True))
    objective_type = db.relationship('ObjectiveType',backref=db.backref('objective_question', lazy=True))