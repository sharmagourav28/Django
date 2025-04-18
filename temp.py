from sqlalchemy import Column, Integer, String, create_engine # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker # type: ignore

from sqlalchemy.engine import URL # type: ignore

# Define base class
Base = declarative_base()

"""
declarative_base() is a factory function provided 
by SQLAlchemy that returns a base class. This base 
class is used to create ORM-mapped classes 
(like Student in our example).

In Java Hibernate, you might annotate a class with @Entity.
Similarly in Python with SQLAlchemy:

Base = declarative_base()  # Base class like a blueprint
All your ORM classes should inherit from this base:

"""


# Define a Student class that will become a table

"""
in the following syntax

id = Column(Integer, primary_key=True)

SQLAlchemy automatically assumes:

    autoincrement=True
    
    what if we don't want auto increment , we want to pass
    id explicitly
    
id = Column(Integer, primary_key=True, autoincrement=False)  # explicitly turned off
"""
class Student(Base):
    __tablename__ = 'student'  # correct way

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


# Connect to MySQL database

"""

pymysql is a pure Python MySQL client library that 
allows your Python code to connect to a MySQL database 
and execute SQL queries.

"echo=True" means python will show you all the database
queries executed by it internally

"""
url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Gourav@2806",  # special characters handled safely
    host="localhost",
    database="pythondb1"
)

engine = create_engine(url, echo=True)
# Automatically create the table(s)
"""
When you call "Base.metadata.create_all(engine), SQLAlchemy:"

    Looks at all subclasses (like Student, Employee, etc.)
    Extracts their table definitions
    Creates corresponding tables in the database.

"""
Base.metadata.create_all(engine)

# Create a session

"""
sessionmaker is a factory for creating new Session objects.

You're telling SQLAlchemy:
"Create a class called Session that knows how to 
connect to the database using the engine."

You're not connecting yet—you're just setting up 
the recipe for making sessions

"""
Session = sessionmaker(bind=engine)

"""
session = Session()

    This creates an actual session instance.
    A Session is the main way to:
    Talk to the database
    Query and add records
    Manage transactions (commit, rollback)
    You use this session object to interact with the database like:
    
    session.add(new_employee)
    session.commit()
    employees = session.query(Employee).all()

"""
session = Session()

# Add a student
student1 = Student(name="Rohit", age=21)
student2 = Student(name="Vishal", age=23)
student3 = Student(name="Priti", age=25)
session.add(student1)
session.add(student2)
session.add(student3)

session.commit()   # is compulsory

# Query the student

"""
all() is a method that executes the query and 
returns all results as a list.

Each item in the list is an instance of the Student model.
"""
all_students = session.query(Student).all()
for s in all_students:
    print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}")


"""
What else can be there instead of "all()" method?

ans:

# Get the first student only
first_student = session.query(Student).first()

# Get a limited number of students (e.g., 5)
limited_students = session.query(Student).limit(5).all()

# Get count of students
student_count = session.query(Student).count()
"""