"""
lazy='joined'  is for eager fetch

lazy='select' [ by default ] is for lazy fetch

notice the fat query when you query for company

it will fire 1 query for company and n queries for
employee. This is called as "n+1" problem
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey # type: ignore

from sqlalchemy.orm import declarative_base, relationship, sessionmaker # type: ignore
from sqlalchemy.engine import URL # type: ignore
# Base class
Base = declarative_base()

# Company model
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # One-to-many relationship
    employees = relationship('Employee', back_populates='company',cascade='all, delete',lazy='joined')

# Employee model
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))

    # Reference back to company
    company = relationship('Company', back_populates='employees')


# MySQL connection string: update username, password, and dbname as needed
url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Gourav@2806",  # special characters handled safely
    host="localhost",
    database="pythondb1"
)

engine = create_engine(url, echo=True)
# Automatically create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create company and employees
company1 = Company(name="Capgemini")
emp1 = Employee(name="SRK", company=company1)
emp2 = Employee(name="Aamir", company=company1)
emp3 = Employee(name="Akshay", company=company1)

# Add to session and commit
session.add(company1)
session.commit()

# Retrieve company with employees

"""
results = session.query(Company).all()
for company in results:
    print(f"Company: {company.name}")
    for emp in company.employees:
        print(f"Employee: {emp.name}")

"""

result = session.query(Company).filter_by(name="Capgemini").first()
print(f"Company name is : {result.name}")
for emp in result.employees:
    print(f"Employee: {emp.name}")
