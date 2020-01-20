class Student:

    def __init__(self, slack_handle, first_name, last_name, student_cohort):
        self.slack_handle = slack_handle
        self.first_name = first_name
        self.last_name = last_name
        self.student_cohort = student_cohort
        self.student_exercises = list()