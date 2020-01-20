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

# Create 3, or more, cohorts.

cohort1 = Cohort("Cohort 1", "123", "001")
cohort2 = Cohort("Cohort 2", "456", "002")
cohort3 = Cohort("Cohort 3", "789", "003")

# Create 4, or more, students and assign them to one of the cohorts.

student1 = Student("Bob", "Bob", "Builder", cohort1)


# Create 3, or more, instructors and assign them to one of the cohorts.
# Have each instructor assign 2 exercises to each of the students.

for prop, value in cohort1.__dict__.items():
    print(f'{prop}:\n{value}\n')