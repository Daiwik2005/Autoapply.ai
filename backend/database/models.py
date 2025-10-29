from sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Resume(db.Model):
    resume=db.Column(db.string(200),unique=False,nullable=False)
    