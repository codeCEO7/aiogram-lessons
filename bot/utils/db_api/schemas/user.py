import os

from sqlalchemy import create_engine, Column, Integer, Boolean, String
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker

load_dotenv()

host = str(os.getenv("HOST"))
password = str(os.getenv("PASSWORD"))
database = str(os.getenv("DATABASE"))

engine = create_engine(f"postgresql+psycopg2://postgres:{password}@{host}/{database}")

session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    admin = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
