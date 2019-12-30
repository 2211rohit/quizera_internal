from .. import db
class Section(db.Model):
    """[Create Section Table]  
    Args:
        db ([type]): [description]
    """
    __tablename__ = 'section'
    section_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    section_name = db.Column(db.String(250), unique=True, nullable=False)
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.batch_id'),nullable=False)
    batch = db.relationship('Batch',backref=db.backref('section', lazy=True))