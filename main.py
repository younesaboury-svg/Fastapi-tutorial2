from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
    )
class student(BaseModel):
    id: int
    name: str
    grade: int
students = [
    student(id=1, name="Alice", grade=5),
    student(id=2, name="Bob", grade=9),
]
@app.get("/students/")
def read_students():
    return students
@app.post("/students/")
def create_student(New_student: student):
    students.append(New_student)
    return New_student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted "}
    return {"error": "Student not found"}
