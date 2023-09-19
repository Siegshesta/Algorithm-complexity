class Student:
    """A class to represent a student."""

    # Class attributes
    full_name = ""
    id = 0
    s_course = 1
    s_faculty = ""
    speciality = ""
    is_local_student = False
    subjects = []
    semester = 1

    def __init__(self, name, surname, student_id, course, faculty, speciality):
        """Initializes a new student object.

        Args:
            name: The student's name.
            surname: The student's surname.
            student_id: The student's student ID.
            course: The student's course.
            faculty: The student's faculty.
            speciality: The student's speciality.
        """

        self.full_name = f"{name} {surname}"
        self.id = student_id
        self.s_course = course
        self.s_faculty = faculty
        self.speciality = speciality

    def all_info(self):
        """Prints all fields of the student object."""

        print(f"Full name: {self.full_name}")
        print(f"Student ID: {self.id}")
        print(f"Course: {self.s_course}")
        print(f"Faculty: {self.s_faculty}")
        print(f"Speciality: {self.speciality}")
        print(f"Is local student: {self.is_local_student}")
        print(f"Subjects: {self.subjects}")
        print(f"Semester: {self.semester}")

    def get_full_name(self):
        """Returns the student's full name."""

        return self.full_name

    def add_subject(self, subject):
        """Adds a subject to the list of student subjects.

        Args:
            subject: The subject to add.
        """

        self.subjects.append(subject)

    def transfer_to_next_semester(self):
        """Increments the semester field by one and updates the course accordingly.

        If the semester is 7, the course is updated to 3.
        """

        self.semester += 1

        if self.semester == 7:
            self.s_course = 3

        # Empty all current subjects
        self.subjects = []

# Create 3 object instances
student1 = Student("Zhamilya", "Akan", 123456, 3, "Computer Science", "Software Engineering")
student2 = Student("Alexander", "Yu", 654321, 2, "Mathematics", "Applied Mathematics")
student3 = Student("Edik", "Kim", 789012, 3, "Economics", "Finance")

# Demonstrate all methods
print("Student 1:")
student1.all_info()

print("Student 2:")
student2.all_info()

print("Student 3:")
student3.all_info()

# Add a subject to student 1
student1.add_subject("Python Programming")

# Transfer student 1 to the next semester
student1.transfer_to_next_semester()

# Print student 1's full name
print(student1.get_full_name())

# Print student 1's subjects
print(student1.subjects)

