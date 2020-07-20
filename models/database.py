from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # ?
from sqlalchemy.orm import sessionmaker  # ?

# 3. Як це брати з файлу?
db_string = "postgres://nataliia:nat_postgres_88@localhost:5432/nataliia"

db = create_engine(db_string)
base = declarative_base()

Session = sessionmaker(db)
session = Session()
