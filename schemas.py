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
   pass

class StudyHabitsBase(BaseModel):
    Study_Hours_per_Week: Optional[int] = None
    Sleep_Hours_per_Night: Optional[float] = None
    Stress_Level: Optional[int] = None

class ExtracurricularsBase(BaseModel):
    Extracurricular_Activities: Optional[bool] = None

class FamilyBackgroundBase(BaseModel):
    Internet_Access_at_Home: Optional[bool] = None
    Parent_Education_Level: Optional[str] = None
    Family_Income_Level: Optional[str] = None

class AcademicDetails(AcademicDetailsBase):
    Student_ID: str

    class Config:
        orm_mode = True

class StudyHabits(StudyHabitsBase):
    Student_ID: str

    class Config:
        orm_mode = True

class Extracurriculars(ExtracurricularsBase):
    Student_ID: str

    class Config:
        orm_mode = True

class FamilyBackground(FamilyBackgroundBase):
    Student_ID: str

    class Config:
        orm_mode = True

class Student(StudentBase):
    Student_ID: str
    academic_details: Optional[AcademicDetails] = None
    study_habits: Optional[StudyHabits] = None
    extracurriculars: Optional[Extracurriculars] = None
    family_background: Optional[FamilyBackground] = None

    class Config:
        orm_mode = True

class StudentFeatures(BaseModel):
    Gender: int
    Age: int
    Department: int
    Attendance: float
    Midterm_Score: float
    Final_Score: float
    Assignments_Avg: float
    Quizzes_Avg: float
    Participation_Score: float
    Projects_Score: float
    Grade: int
    Study_Hours_per_Week: float
    Extracurricular_Activities: int
    Internet_Access_at_Home: int
    Family_Income_Level: int
    Stress_Level: int
    Sleep_Hours_per_Night: float