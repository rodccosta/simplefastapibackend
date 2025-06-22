from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.person import PersonCreate
from models.person import Person

skip = 0
limit = 100

router = APIRouter(prefix="/api/person", tags=["Pessoa"])

@router.get("/")
def getPersons(db: Session = Depends(get_db)):
    try:
        return db.query(Person).offset(skip).limit(limit).all()
    except Exception as e:
        print("Error: ", e)
        return {"message": "User fetch failed"}

@router.get("/{person_id}")
def getPerson(person_id: int, db: Session = Depends(get_db)):
    return db.query(Person).filter(Person.id == person_id).first()

@router.post("/", status_code=201)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    db_person = Person(**person.model_dump())
    db.add(db_person)
    try:
        db.commit()
        db.refresh(db_person)
        return db_person
    except Exception as e:
        db.rollback()
        return {"message": "Error creating person", "error": str(e)}

@router.delete("/{person_id}", status_code=204)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    db.delete(person)
    db.commit()
    return



