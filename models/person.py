from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String, Date
from database import Base
# model
class Person(Base):
    __tablename__= "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    birthday = Column(Date)