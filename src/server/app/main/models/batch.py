from .. import db

class Batch(db.Model):
    """[summary]   
    Args:
        db ([type]): [description]
    """
    __tablename__ = 'batch'
    batch_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    batch_name = db.Column(db.String(250), unique=True, nullable=False)