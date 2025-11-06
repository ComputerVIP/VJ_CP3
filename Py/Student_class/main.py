#VJ Student Class

class Student:
    def __init__(self, name="John Doe",student_id=000, grade=100):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def update_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.grade = new_grade
            return f"Grade updated to {self.grade}"
        else:
            return "Invalid grade. Please enter a value between 0 and 100."
    
    def get_grade(self):
        return self.grade
    
    def __str__(self):
        return f"Student(Name: {self.name}, ID: {self.student_id}, Grade: {self.grade})"
    

student1 = Student("Alice", 1, 95)
student2 = Student("Dave", 2, 88)
student3 = Student("Dove", 3, 99)
student4 = Student("Deve", 4, 78)
student5 = Student()  # Uses default values

for student in [student1, student2, student3, student4, student5]:
    print(student)

print(student5.get_grade())
print(student5.update_grade(90))
print(student2.update_grade(100))
print(student3.update_grade(105))  # Invalid grade
print(student1.update_grade(85))
print(student1.update_grade(-10))  # Invalid grade