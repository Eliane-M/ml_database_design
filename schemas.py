from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    First_Name: Optional[str] = None
    Last_Name: Optional[str] = None
    Email: Optional[str] = None
    Gender: Optional[str] = None
    Age: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    Student_ID: str

    class Config:
        orm_mode = True

class AcademicDetailsBase(BaseModel):
    Department: Optional[str] = None
    Attendance_Percentage: Optional[float] = None
    Midterm_Score: Optional[float] = None
    Final_Score: Optional[float] = None
    Assignments_Avg: Optional[float] = None
    Quizzes_Avg: Optional[float] = None
    Participation_Score: Optional[float] = None
    Projects_Score: Optional[float] = None
    Total_Score: Optional[float] = None
    Grade: Optional[str] = None

class AcademicDetailsCreate(AcademicDetailsBase):
    Student_ID: str

class AcademicDetails(AcademicDetailsBase):
    Student_ID: str

    class Config:
        orm_mode = True