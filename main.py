from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student


"""
Objective
The learning objective of this exercise is to practice creating instances of custom types that you defined with class, establishing the relationships between them, and practicing basic data structures in Python. """

# Create 4, or more, exercises.
first_exercise = Exercise("Intro to Python 1", "Python")
second_exercise = Exercise("Intro to Python 2", "Python")
third_exercise = Exercise("Intro to Python 3", "Python")
fourth_exercise = Exercise("Intro to Python 4", "Python")
fifth_exercise = Exercise("Intro to Python 5", "Python")
sixth_exercise = Exercise("Intro to Python 6", "Python")

# Create 3, or more, cohorts.

cohort1 = Cohort("Cohort 1", "123", "001")
cohort2 = Cohort("Cohort 2", "456", "002")
cohort3 = Cohort("Cohort 3", "789", "003")

# Create 4, or more, students and assign them to one of the cohorts.

student1 = Student("slack_Bob", "Bob", "Builder", cohort1)
student2 = Student("slack_John", "John", "Doe", cohort1)
student3 = Student("slack_Jane", "Jane", "Doe", cohort1)
student4 = Student("slack_Wookie", "Wookie", "Wooks", cohort1)
students_list = [student1, student2, student3, student4]

# Create 3, or more, instructors and assign them to one of the cohorts.

instructor1 = Instructor(cohort1)
instructor2 = Instructor(cohort1)
instructor3 = Instructor(cohort1)
instructors_list = [instructor1, instructor2, instructor3]

# Have each instructor assign 2 exercises to each of the students.

for student in students_list:
    instructor1.assign_exercise(student,
    [first_exercise.exercise_name, second_exercise.exercise_name])
for student in students_list:
    instructor2.assign_exercise(student,
    [third_exercise.exercise_name, fourth_exercise.exercise_name])
for student in students_list:
    instructor2.assign_exercise(student,
    [fifth_exercise.exercise_name, sixth_exercise.exercise_name])

for prop, value in student1.__dict__.items():
    print(f'{prop}:\n{value}\n')