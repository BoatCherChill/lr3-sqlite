from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LR3 — SQLite Database")

@app.post("/students", response_model=schemas.StudentOut, status_code=201)
def create_student(data: schemas.StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Student).filter(models.Student.email == data.email).first()
    if existing:
        raise HTTPException(400, "Студент с таким email уже есть")

    new_student = models.Student(name=data.name, email=data.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students", response_model=list[schemas.StudentOut])
def list_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@app.get("/students/{student_id}", response_model=schemas.StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(404, "Студент не найден")
    return student

@app.put("/students/{student_id}", response_model=schemas.StudentOut)
def update_student(student_id: int, data: schemas.StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(404, "Студент не найден")

    student.name = data.name
    db.commit()
    db.refresh(student)
    return student

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(404, "Студент не найден")

    db.delete(student)
    db.commit()
    return None