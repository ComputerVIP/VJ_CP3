#VJ Student Class

class Student:
    def __init__(self, name="John Doe",student_id=000, grade=100):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}")