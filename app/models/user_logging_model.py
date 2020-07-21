from sqlalchemy import ForeignKey, Column, Integer, DateTime, func
from sqlalchemy.orm import relationship

from .database import base, session
from .user_model import UserModel


class UserLoggingModel(base):
    __tablename__ = 'user_loggings'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'),
                                nullable=False,
                                index=True)
    log_datetime = Column(DateTime, default=func.now())

    users = relationship(UserModel)

    def save_to_db(self):
        session.add(self)
        session.commit()
