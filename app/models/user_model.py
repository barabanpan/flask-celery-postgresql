from .database import base, session
from sqlalchemy import Column, String, Integer
from passlib.hash import pbkdf2_sha256 as sha256


class UserModel(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

    # 3. Is there something more natural than class methods?
    @classmethod
    def find_by_username(cls, username):
        return session.query(cls).filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), session.query(cls)))}

    @classmethod
    def delete_all(cls):
        try:
            # ????????
            num_rows_deleted = session.query(cls).delete()
            session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except Exception:
            return {'message': 'Something went wrong while deleting all'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def save_to_db(self):
        session.add(self)
        session.commit()
