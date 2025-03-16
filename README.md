# ML Database Design Formative Assignment

## Overview

This project provides a FastAPI-based web service for managing a student database. The API allows you to create, read, update, and delete student data such as their info, academic history and more.

## Link to the ERD Diagram
[Link](https://docs.google.com/document/d/1xDpYWynzNSU_wvh1TCrWlSaNk-pWvK2GxdJD9APbZBs/edit?usp=sharing) to the report with the ERD diagram

## Dataset used

We used a [dataset](https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset) from Kaggle with 5000 records about student performance based on their school routines and family background.

## Deployment

The API is deployed and accessible at [Student Management Apis](https://ml-database-design.onrender.com)

## Database Schema

The database consists of the following tables:

### 1. Student  
- `student_id` (Primary Key)  
- `first_name`  
- `last_name`  
- `email`  
- `gender`  

### 2. Study_Habits  
- `student_id` (Primary Key, Foreign Key)  
- `study_hours_per_week`  
- `preferred_study_method`  
- `use_of_technology`  
- `group_study_participation`  

### 3. Academic_Details  
- `student_id` (Primary Key, Foreign Key)  
- `department`  
- `attendance_percentage`  
- `midterm_score`  
- `final_score`  
- `assignment_avg`  
- `quizzes_avg`  
- `participation_score`  
- `projects_score`  
- `total_score`  
- `grade`  

### 4. Extracurriculars  
- `student_id` (Primary Key, Foreign Key)  
- `extracurricular_activities`  

### 5. Family_Background  
- `student_id` (Primary Key, Foreign Key)  
- `internet_access_at_home`  
- `parent_education_level`  
- `family_income_level`  

### 6. Student_Audit_Log  
- `log_id` (Primary Key, Auto Increment)  
- `student_id` (Foreign Key)  
- `old_email`  
- `new_email`  
- `change_time`  
- `action`

## Technologies Used

- FastAPI
- MySQL
- Python3

## Installation
To try it out on you own follow the following steps:

```
git clone https://github.com/Eliane-M/ml_database_design.git
```

```
cd ml_database_design
```

create a virtual environment and activate it

```
python -m venv venv
```

```
source venv/Scripts/activate
```

install dependencies

```
pip install -r requirements.txt
```


## API Endpoints

`POST /students/` - Create a new student with basic information only  
`POST /students/details/` - Create a student with detailed information such as academic records, family background and lifestyle factors 
`GET /students/` - List all students  
`GET /students/latest/` - Get last student in the database
`GET /students/predict/` - Predict total score of last student
`GET /students/{student_id}` - Get a specific student  
`PUT /students/{student_id}` - Update a student  
`DELETE /students/{student_id}` - Delete a student

For more detailed information, refer to the swagger documentation available at [Student Management Apis](https://ml-database-design.onrender.com)

## Contributors

- Eliane Munezero (Database creation)
- Bernice Uwituze (API implementation)
- Kangabire Muhoza Merveille (Model And Predictions)


