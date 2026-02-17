from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


students = []


class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str


@app.get("/students")
def get_students():
    return students


@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully"}


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {"message": "Student updated successfully"}
    return {"error": "Student not found"}



@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}
    return {"error": "Student not found"}
