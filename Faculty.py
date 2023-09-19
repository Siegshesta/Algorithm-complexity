class Faculty:
    """A class to represent a faculty."""

    def __init__(self, name, dean, cabinet_number):
        """Initializes a new faculty object.

        Args:
            name: The name of the faculty.
            dean: The dean of the faculty.
            cabinet_number: The cabinet number of the dean.
        """

        self.faculty_name = name
        self.dean = dean
        self.students = []
        self.cabinet_number = cabinet_number

    def add_student(self, student):
        """Adds a student to the list of students in the faculty.

        Args:
            student: The student to add.
        """

        self.students.append(student)

    def withdraw_student(self, student_id):
        """Removes a student from the list of students in the faculty.

        Args:
            student_id: The student ID of the student to remove.
        """

        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return

        print("Student with ID {} not found.".format(student_id))

# Create at least 2 faculties
faculty1 = Faculty("Business administration", "Dr. Medetov Dan", 123)
faculty2 = Faculty("IT", "Dr. Saulet Yerbolatovna", 456)

# Demonstrate methods by printing
print("Faculty 1:")
print(f"Name: {faculty1.faculty_name}")
print(f"Dean: {faculty1.dean}")
print(f"Cabinet number: {faculty1.cabinet_number}")
print(f"Students: {faculty1.students}")

print("Faculty 2:")
print(f"Name: {faculty2.faculty_name}")
print(f"Dean: {faculty2.dean}")
print(f"Cabinet number: {faculty2.cabinet_number}")
print(f"Students: {faculty2.students}")
