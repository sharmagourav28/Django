from sqlalchemy import create_engine, Column, Integer, String # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from sqlalchemy.engine import URL # type: ignore

# Replace with your own MySQL details
url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Gourav@2806",  # special characters handled safely
    host="localhost",
    database="pythondb1"
)

engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the table (if it doesn't exist)
Base.metadata.create_all(engine)
