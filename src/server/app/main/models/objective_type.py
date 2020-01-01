from .. import db


class ObjectiveType(db.Model):
    """[summary]   
    Args:
        db ([type]): [description]
    """
    __tablename__ = 'objective_type'
    objective_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    objective_type = db.Column(db.String(250), unique=True, nullable=False)