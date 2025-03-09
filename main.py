from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency to get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API routes

# Create student
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student.Student_ID)
    if db_student:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    return crud.create_student(db, student)

# Create student with details
@app.post("/students/details/", response_model=schemas.Student)
def create_student_with_details(
    student: schemas.StudentCreate,
    academic: schemas.AcademicDetailsCreate,
    study_hours: int,
    sleep_hours: float,
    stress_level: int,
    extracurricular: bool,
    internet_access: bool,
    parent_education: str,
    family_income: str,
    db: Session = Depends(get_db)
):
    db_student = crud.get_student(db, student.Student_ID)
    if db_student:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    return crud.create_student_with_details(
        db, student, academic, study_hours, sleep_hours, stress_level, extracurricular, internet_access, parent_education, family_income
    )

# Get all students
@app.get("/students/", response_model=list[schemas.Student])
def get_all_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

# Get student by id
@app.get("/students/{student_id}", response_model=schemas.Student)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update student
@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": f"Student {student_id} deleted successfully"}