from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

PATH='postgresql://postgres:postgres@localhost:5432/db'

engine = create_engine(PATH, echo=True)


Base= declarative_base()

session=sessionmaker(bind=engine)