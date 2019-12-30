from .. import db

class Batch(db.Model):
    __tablename__ = 'batch'
    """[Create Batch Table]
    """
    batch_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    batch_name = db.Column(db.String(250), unique=True, nullable=False)