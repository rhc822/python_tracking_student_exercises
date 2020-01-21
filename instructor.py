class Instructor:

    def __init__(self, instructor_cohort):
        self.slack_handle = ""
        self.first_name = ""
        self.last_name = ""
        self.instructor_cohort = instructor_cohort
        self.instructor_specialty = ""

# Method to assign student an exercise
    def assign_exercise(self, student, exercises):
        student.student_exercises.extend(exercises)
