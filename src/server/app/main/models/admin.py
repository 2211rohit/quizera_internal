from .. import db


class Admin(db.Model):
    __tablename__ = 'admin'
    """[Create Admin Table]
    """
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_name = db.Column(db.String(250), unique=True, nullable=False)