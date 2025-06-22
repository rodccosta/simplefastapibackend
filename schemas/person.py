from pydantic import BaseModel
from datetime import date

class PersonCreate(BaseModel):
    name: str
    birthday: date

