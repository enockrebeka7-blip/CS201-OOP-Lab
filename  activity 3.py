# Student class
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


# Gradebook class
class Gradebook:
    def __init__(self):
        # initialize empty list
        self.students = []

    # add student to the list
    def add_student(self, student):
        self.students.append(student)

    # calculate class average
    def get_average(self):
        if len(self.students) == 0:
            return 0

        total = 0
        for student in self.students:
            total += student.score

        average = total / len(self.students)
        return average


# ---- Testing the program ----
student1 = Student("Alice", 80)
student2 = Student("Bob", 70)
student3 = Student("John", 90)

gradebook = Gradebook()
gradebook.add_student(student1)
gradebook.add_student(student2)
gradebook.add_student(student3)

print("Class Average:", gradebook.get_average())