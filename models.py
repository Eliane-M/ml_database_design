from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.types import DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = "Students"
    Student_ID = Column(String(10), primary_key=True)
    First_Name = Column(String(50))
    Last_Name = Column(String(50))
    Email = Column(String(100))
    Gender = Column(String(1))
    Age = Column(Integer)

    academic_details = relationship("AcademicDetails", back_populates="student", uselist=False)
    study_habits = relationship("StudyHabits", back_populates="student", uselist=False)
    extracurriculars = relationship("Extracurriculars", back_populates="student", uselist=False)
    family_background = relationship("FamilyBackground", back_populates="student", uselist=False)

    @staticmethod
    def generate_student_id(db: Session):
        last_student = db.query(Student).order_by(Student.Student_ID.desc()).first()
        if last_student:
            last_id_num = int(last_student.Student_ID[1:])
            new_id_num = last_id_num + 1
        else:
            new_id_num = 1
        return f"S{new_id_num:04d}"

class AcademicDetails(Base):
    __tablename__ = "Academic_Details"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Department = Column(String(50))
    Attendance_Percentage = Column(DECIMAL(5, 2))
    Midterm_Score = Column(DECIMAL(5, 2))
    Final_Score = Column(DECIMAL(5, 2))
    Assignments_Avg = Column(DECIMAL(5, 2))
    Quizzes_Avg = Column(DECIMAL(5, 2))
    Participation_Score = Column(DECIMAL(5, 2))
    Projects_Score = Column(DECIMAL(5, 2))
    Total_Score = Column(DECIMAL(5, 2))
    Grade = Column(String(2))

    student = relationship("Student", back_populates="academic_details")


class StudyHabits(Base):
    __tablename__ = "Study_Habits"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Study_Hours_per_Week = Column(Integer)
    Sleep_Hours_per_Night = Column(DECIMAL(3, 1))
    Stress_Level = Column(Integer)
    __table_args__ = (CheckConstraint("Stress_Level BETWEEN 1 AND 10"),)

    student = relationship("Student", back_populates="study_habits")

class Extracurriculars(Base):
    __tablename__ = "Extracurriculars"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Extracurricular_Activities = Column(Boolean)

    student = relationship("Student", back_populates="extracurriculars")

class FamilyBackground(Base):
    __tablename__ = "Family_Background"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Internet_Access_at_Home = Column(Boolean)
    Parent_Education_Level = Column(String(50))
    Family_Income_Level = Column(String(50))

    student = relationship("Student", back_populates="family_background")

class StudentAuditLog(Base):
    __tablename__ = "Student_Audit_Log"
    Log_ID = Column(Integer, primary_key=True, autoincrement=True)
    Student_ID = Column(String(10))
    Old_Email = Column(String(100))
    New_Email = Column(String(100))
    Change_Time = Column(DateTime)
    Action = Column(String(50))