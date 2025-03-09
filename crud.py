from sqlalchemy.orm import Session
import models, schemas

# get all students
def get_students(db: Session):
    return db.query(models.Student).all()

# get student by id
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.Student_ID == student_id).first()

# create student
def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def create_student_with_details(
    db: Session,
    student: schemas.StudentCreate,
    academic: schemas.AcademicDetailsCreate,
    study_hours: int,
    sleep_hours: float,
    stress_level: int,
    extracurricular: bool,
    internet_access: bool,
    parent_education: str,
    family_income: str
):
    db.execute(
        "CALL AddNewStudent(:p_Student_ID, :p_First_Name, :p_Last_Name, :p_Email, :p_Gender, :p_Age, "
        ":p_Department, :p_Attendance_Percentage, :p_Midterm_Score, :p_Final_Score, :p_Assignments_Avg, "
        ":p_Quizzes_Avg, :p_Participation_Score, :p_Projects_Score, :p_Total_Score, :p_Grade, "
        ":p_Study_Hours_per_Week, :p_Sleep_Hours_per_Night, :p_Stress_Level, :p_Extracurricular_Activities, "
        ":p_Internet_Access_at_Home, :p_Parent_Education_Level, :p_Family_Income_Level)",
        {
            "p_Student_ID": student.Student_ID,
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
    return get_student(db, student.Student_ID)

# update student
def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    student_to_update = db.query(models.Student).filter(models.Student.Student_ID == student_id).first()
    if not student_to_update:
        return None
    for key, value in student.dict(exclude_unset=True).items():
        setattr(student_to_update, key, value)
    db.commit()
    db.refresh(student_to_update)
    return student_to_update

# delete student
def delete_student(db: Session, student_id: int):
    student_to_delete = db.query(models.Student).filter(models.Student.Student_ID == student_id).first()
    if not student_to_delete:
        return None
    db.delete(student_to_delete)
    db.commit()
    return student_to_delete

