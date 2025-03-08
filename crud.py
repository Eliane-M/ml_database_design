from sqlalchemy.orm import Session
# import models, schemas

# get all students
def get_students(db: Session):
    return db.query(models.Student).all()

# get student by id
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

# create student
def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# update student


