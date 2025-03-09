from sqlalchemy import Column, String, Integer, Decimal, Boolean, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    Student_ID = Column(String(10), primary_key=True)
    First_Name = Column(String(50))
    Last_Name = Column(String(50))
    Email = Column(String(100))
    Gender = Column(String(1))
    Age = Column(Integer)

class AcademicDetails(Base):
    __tablename__ = "Academic_Details"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Department = Column(String(50))
    Attendance_Percentage = Column(Decimal(5, 2))
    Midterm_Score = Column(Decimal(5, 2))
    Final_Score = Column(Decimal(5, 2))
    Assignments_Avg = Column(Decimal(5, 2))
    Quizzes_Avg = Column(Decimal(5, 2))
    Participation_Score = Column(Decimal(5, 2))
    Projects_Score = Column(Decimal(5, 2))
    Total_Score = Column(Decimal(5, 2))
    Grade = Column(String(2))


class StudyHabits(Base):
    __tablename__ = "Study_Habits"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Study_Hours_per_Week = Column(Integer)
    Sleep_Hours_per_Night = Column(Decimal(3, 1))
    Stress_Level = Column(Integer)
    __table_args__ = (CheckConstraint("Stress_Level BETWEEN 1 AND 10"),)

class Extracurriculars(Base):
    __tablename__ = "Extracurriculars"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Extracurricular_Activities = Column(Boolean)

class FamilyBackground(Base):
    __tablename__ = "Family_Background"
    Student_ID = Column(String(10), ForeignKey("Students.Student_ID"), primary_key=True)
    Internet_Access_at_Home = Column(Boolean)
    Parent_Education_Level = Column(String(50))
    Family_Income_Level = Column(String(50))

class StudentAuditLog(Base):
    __tablename__ = "Student_Audit_Log"
    Log_ID = Column(Integer, primary_key=True, autoincrement=True)
    Student_ID = Column(String(10))
    Old_Email = Column(String(100))
    New_Email = Column(String(100))
    Change_Time = Column(DateTime)
    Action = Column(String(50))