class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f"{self.name} (ID: {self.id_number})"

class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self):
        return f"Student: {self.name}, Major: {self.major} (ID: {self.id_number})"

class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f"Instructor: {self.name}, Department: {self.department} (ID: {self.id_number})"

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def __str__(self):
        return f"Course: {self.course_name} (ID: {self.course_id})"

class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"Enrollment: {self.student.name} in {self.course.course_name} - Grade: {self.grade if self.grade is not None else 'Not Assigned'}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.instructors = {}
        self.courses = {}
        self.enrollments = []

    def add_student(self, student):
        self.students[student.id_number] = student

    def remove_student(self, student):
        if student.id_number in self.students:
            del self.students[student.id_number]
            # Remove from any courses
            for course in self.courses.values():
                course.remove_student(student)
            # Remove enrollments
            self.enrollments = [e for e in self.enrollments if e.student.id_number != student.id_number]

    def update_student(self, student_id, name=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name is not None:
                student.name = name
            if major is not None:
                student.major = major

    def add_instructor(self, instructor):
        self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, instructor):
        if instructor.id_number in self.instructors:
            del self.instructors[instructor.id_number]

    def update_instructor(self, instructor_id, name=None, department=None):
        if instructor_id in self.instructors:
            instructor = self.instructors[instructor_id]
            if name is not None:
                instructor.name = name
            if department is not None:
                instructor.department = department

    def add_course(self, course):
        self.courses[course.course_id] = course

    def remove_course(self, course):
        if course.course_id in self.courses:
            del self.courses[course.course_id]
            # Remove students from the course
            for student in course.enrolled_students:
                student_course_enrollments = [e for e in self.enrollments if e.course.course_id == course.course_id and e.student.id_number == student.id_number]
                for enrollment in student_course_enrollments:
                    self.enrollments.remove(enrollment)

    def update_course(self, course_id, course_name=None):
        if course_id in self.courses:
            course = self.courses[course_id]
            if course_name is not None:
                course.course_name = course_name

    def enroll_student(self, student, course):
        if student.id_number in self.students and course.course_id in self.courses:
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)

    def assign_grade(self, student, course, grade):
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student.id_number and enrollment.course.course_id == course.course_id:
                enrollment.assign_grade(grade)
                break

    def get_students_in_course(self, course):
        return course.enrolled_students

    def get_courses_of_student(self, student):
        student_courses = [e.course for e in self.enrollments if e.student.id_number == student.id_number]
        return student_courses

# Example usage:

# Creating instances
s1 = Student("Nike", "S001", "Computer Science")
s2 = Student("Grace", "S002", "Mathematics")
s3 = Student("Tope", "S003", "Linguistics")
s4 = Student("Yemi", "S004", "Geophysics")

i1 = Instructor("Dr. Idowu", "I001", "Computer Science")
i2 = Instructor("Dr. James", "I002", "Mathematics")
i3 = Instructor("Dr. Dada", "I003", "Linguistics")
i4 = Instructor("Dr. Ibrahim", "I004", "Geophysics")

c1 = Course("Algorithms", "C001")
c2 = Course("Calculus", "C002")
c3 = Course("English", "C003")
c4 = Course("Physics", "C004")



# Managing the system
system = StudentManagementSystem()
system.add_student(s1)
system.add_student(s2)
system.add_student(s3)
system.add_student(s4)

system.add_instructor(i1)
system.add_instructor(i2)
system.add_instructor(i3)
system.add_instructor(i4)

system.add_course(c1)
system.add_course(c2)
system.add_course(c3)
system.add_course(c4)

# Enrolling students
system.enroll_student(s1, c1)
system.enroll_student(s2, c2)
system.enroll_student(s3, c3)
system.enroll_student(s4, c4)

# Assigning grades
system.assign_grade(s1, c1, "A")
system.assign_grade(s2, c2, "B")
system.assign_grade(s3, c3, "B")
system.assign_grade(s4, c4, "B")

# Retrieving information
print(system.get_students_in_course(c1))  
print(system.get_courses_of_student(s1))  