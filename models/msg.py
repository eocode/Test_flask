from sqlalchemy import Column, Integer, String, DateTime
from app.database.db_instance import db
from sqlalchemy.event import listen


class Msg(db.Model):
    """Simple model example"""

    __tablename__ = 'msgs'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=True)
    created_at = db.Column(DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(
        DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, name=None):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __str__(self):
        return self.name
