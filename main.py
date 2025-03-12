from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas, crud
from typing import Dict, Optional

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="""API for managing student records with comprehensive features including:
    - Student profile management
    - Academic details tracking
    - Lifestyle factors monitoring
    - Family background information""",
    version="1.0.0",
    docs_url="/",   
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# dependency to get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API routes

# Create student
@app.post("/students/",
           response_model=schemas.Student,
           summary="Create a new student",
    description="Creates a new student record with basic information",
    response_description="The created student record")

def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    """Create a new student with basic information
    
    Args:
        student: Student creation data including email and required fields
    
    Returns:
        The newly created student object
        
    Raises:
        HTTPException: 400 if student with email already exists
    """
    db_student = crud.get_student_by_email(db, student.Email)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already exists")
    return crud.create_student(db, student)

# Create student with details
@app.post("/students/details/", response_model=schemas.Student,
          summary="Create student with detailed information",
    description="Creates a student with comprehensive academic and personal details")
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
    """Create a student with extended details
    
    Args:
        student: Basic student information
        academic: Academic details
        study_hours: Hours spent studying per day
        sleep_hours: Average sleep hours
        stress_level: Stress level (1-10)
        extracurricular: Participation in extracurricular activities
        internet_access: Has internet access at home
        parent_education: Parents' education level
        family_income: Family income bracket
    
    Returns:
        The created student with all details
    """
    student_id = models.Student.generate_student_id(db)
    if student.Email:
        db_student = crud.get_student_by_email(db, student.Email)
        if db_student:
            raise HTTPException(status_code=400, detail="Student already exists")
    
    return crud.create_student_with_details(
        db, student, academic, study_hours, sleep_hours, stress_level, extracurricular, internet_access, parent_education, family_income, generated_student_id=student_id
    )

# Get all students
@app.get("/students/", response_model=list[schemas.Student],
         summary="Get all students",
    description="Retrieve a list of all students in the system")
def get_all_students(db: Session = Depends(get_db)):
    """Fetch all student records
    
    Returns:
        List of all students in the database
    """
    return crud.get_students(db)

# Get student by id
@app.get("/students/{student_id}", response_model=schemas.Student,
         summary="Get student by ID",
    description="Retrieve a student record by ID")
def get_student_by_id(student_id: str, db: Session = Depends(get_db)):
    """Fetch a single student by ID
    
    Args:
        student_id: Unique student identifier
    
    Returns:
        Student object if found
        
    Raises:
        HTTPException: 404 if student not found
    """
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update student
@app.put("/students/{student_id}", response_model=schemas.Student,
         summary="Update student information",
    description="Update specific student details")
def update_student(student_id: str, student_data: Dict[str, object], db: Session = Depends(get_db)):
    """Update student record
    
    Args:
        student_id: Unique student identifier
        student_data: Dictionary of fields to update
    
    Returns:
        Updated student object
        
    Raises:
        HTTPException: 404 if student not found
    """
    updated_student = crud.update_student(db, student_id, student_data)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

# Delete student
@app.delete("/students/{student_id}",summary="Delete a student",
    description="Remove a student from the system")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    """Delete student record
    
    Args:
        student_id: Unique student identifier
    
    Returns:
        Deleted student object
        
    Raises:
        HTTPException: 404 if student not found
    """
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