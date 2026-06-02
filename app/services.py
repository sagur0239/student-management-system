from app.storage import load_data, save_data
from app.models import Student
from app.utils import generate_id
from app.exceptions import StudentNotFoundError

def create_student(name, age, grade):
    data = load_data()
    student_id = generate_id(data)

    student = Student(student_id, name, age, grade)
    data.append(student.to_dict())

    save_data(data)
    return student.to_dict()


def get_all_students():
    return load_data()


def get_student(student_id):
    data = load_data()
    for s in data:
        if s["student_id"] == student_id:
            return s
    raise StudentNotFoundError("Student not found")


def update_student(student_id, name, age, grade):
    data = load_data()
    for s in data:
        if s["student_id"] == student_id:
            s["name"] = name
            s["age"] = age
            s["grade"] = grade
            save_data(data)
            return s
    raise StudentNotFoundError("Student not found")


def delete_student(student_id):
    data = load_data()
    new_data = [s for s in data if s["student_id"] != student_id]

    if len(data) == len(new_data):
        raise StudentNotFoundError("Student not found")

    save_data(new_data)