class Cohort:

    def __init__(self, name, student_list, instructor_list):
        self.cohort_name = name
        self.student_list = list()
        self.instructor_list = list()

    def __str__(self):
        return f"{self.cohort_name}"