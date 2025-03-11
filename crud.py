from sqlalchemy.orm import Session, joinedload
import models, schemas
from fastapi import HTTPException
from typing import Optional
from sqlalchemy.sql import text

# get all students
def get_students(db: Session):
    return db.query(models.Student).options(
        joinedload(models.Student.academic_details),
        joinedload(models.Student.study_habits),
        joinedload(models.Student.extracurriculars),
        joinedload(models.Student.family_background)
    ).all()

# get student by id
def get_student(db: Session, student_id: str):
    return db.query(models.Student).options(
        joinedload(models.Student.academic_details),
        joinedload(models.Student.extracurriculars),
        joinedload(models.Student.family_background),
        joinedload(models.Student.study_habits)
    ).filter(models.Student.Student_ID == student_id).first()

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.Email == email).first()

# create student
def create_student(db: Session, student: schemas.StudentCreate):
    student_id = models.Student.generate_student_id(db)
    new_student = models.Student(Student_ID=student_id, **student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def create_student_with_details(
    db: Session,
    student: schemas.StudentCreate,
    academic: schemas.AcademicDetailsCreate,
    study_hours: Optional[int] = None,
    sleep_hours: Optional[float] = None,
    stress_level: Optional[int] = None,
    extracurricular: Optional[bool] = None,
    internet_access: Optional[bool] = None,
    parent_education: Optional[str] = None,
    family_income: Optional[str] = None,
    generated_student_id: str = None
):
    sql = text(
        "CALL AddNewStudent(:p_Student_ID, :p_First_Name, :p_Last_Name, :p_Email, :p_Gender, :p_Age, "
        ":p_Department, :p_Attendance_Percentage, :p_Midterm_Score, :p_Final_Score, :p_Assignments_Avg, "
        ":p_Quizzes_Avg, :p_Participation_Score, :p_Projects_Score, :p_Total_Score, :p_Grade, "
        ":p_Study_Hours_per_Week, :p_Sleep_Hours_per_Night, :p_Stress_Level, :p_Extracurricular_Activities, "
        ":p_Internet_Access_at_Home, :p_Parent_Education_Level, :p_Family_Income_Level)"
    )
    db.execute(
        sql,
        {
            "p_Student_ID": generated_student_id,
            "p_First_Name": student.First_Name,
            "p_Last_Name": student.Last_Name,
            "p_Email": student.Email,
            "p_Gender": student.Gender,
            "p_Age": student.Age,
            "p_Department": academic.Department,
            "p_Attendance_Percentage": academic.Attendance_Percentage,
            "p_Midterm_Score": academic.Midterm_Score,
            "p_Final_Score": academic.Final_Score,
            "p_Assignments_Avg": academic.Assignments_Avg,
            "p_Quizzes_Avg": academic.Quizzes_Avg,
            "p_Participation_Score": academic.Participation_Score,
            "p_Projects_Score": academic.Projects_Score,
            "p_Total_Score": academic.Total_Score,
            "p_Grade": academic.Grade,
            "p_Study_Hours_per_Week": study_hours,
            "p_Sleep_Hours_per_Night": sleep_hours,
            "p_Stress_Level": stress_level,
            "p_Extracurricular_Activities": extracurricular,
            "p_Internet_Access_at_Home": internet_access,
            "p_Parent_Education_Level": parent_education,
            "p_Family_Income_Level": family_income,
        }
    )
    db.commit()
    return get_student(db, generated_student_id)

# update student
def update_student(db: Session, student_id: str, student_data: dict):
    student_to_update = db.query(models.Student).filter(models.Student.Student_ID == student_id).first()
    if not student_to_update:
        return None
    for key, value in student_data.items():
        if hasattr(student_to_update, key) and key != "Student_ID":
            setattr(student_to_update, key, value)
        else:
            raise HTTPException(status_code=400, detail=f"Invalid field: {key}")
    db.commit()
    db.refresh(student_to_update)
    return student_to_update

# delete student
def delete_student(db: Session, student_id: str):
    student_to_delete = db.query(models.Student).filter(models.Student.Student_ID == student_id).first()
    if not student_to_delete:
        raise HTTPException(status_code=404, detail="Student not found")
    
    try:
        print(f"Deleting AcademicDetails for {student_id}")
        db.query(models.AcademicDetails).filter(models.AcademicDetails.Student_ID == student_id).delete()
        print(f"Deleting StudyHabits for {student_id}")
        db.query(models.StudyHabits).filter(models.StudyHabits.Student_ID == student_id).delete()
        print(f"Deleting Extracurriculars for {student_id}")
        db.query(models.Extracurriculars).filter(models.Extracurriculars.Student_ID == student_id).delete()
        print(f"Deleting FamilyBackground for {student_id}")
        db.query(models.FamilyBackground).filter(models.FamilyBackground.Student_ID == student_id).delete()
        
        print(f"Deleting Student {student_id}")
        db.delete(student_to_delete)
        db.commit()
        return {"message": f"Student {student_id} and all related records deleted successfully"}
    except Exception as e:
        print(f"Error: str{e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting student: {str(e)}")

