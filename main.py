from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas, crud
from typing import Dict, Optional

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
    db_student = crud.get_student_by_email(db, student.Email)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already exists")
    return crud.create_student(db, student)

# Create student with details
@app.post("/students/details/", response_model=schemas.Student)
def create_student_with_details(
    student: schemas.StudentCreate,
    academic: schemas.AcademicDetailsCreate,
    study_hours: Optional[int] = None,
    sleep_hours: Optional[float] = None,
    stress_level: Optional[int] = None,
    extracurricular: Optional[bool] = None,
    internet_access: Optional[bool] = None,
    parent_education: Optional[str] = None,
    family_income: Optional[str] = None,
    db: Session = Depends(get_db)
):
    student_id = models.Student.generate_student_id(db)
    if student.Email:
        db_student = crud.get_student_by_email(db, student.Email)
        if db_student:
            raise HTTPException(status_code=400, detail="Student already exists")
    
    return crud.create_student_with_details(
        db, student, academic, study_hours, sleep_hours, stress_level, extracurricular, internet_access, parent_education, family_income, generated_student_id=student_id
    )

# Get all students
@app.get("/students/", response_model=list[schemas.Student])
def get_all_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

# Get student by id
@app.get("/students/{student_id}", response_model=schemas.Student)
def get_student_by_id(student_id: str, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update student
@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: str, student_data: Dict[str, object], db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, student_data)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# Swagger UI metadata
app = FastAPI(
    title="Student Management API",
    description="This API manages students and their details, including academic records, study habits, extracurriculars, and family background.",
    version="1.0.0",
    docs_url="/", 
    redoc_url="/redoc",  
    openapi_url="/openapi.json",  
)