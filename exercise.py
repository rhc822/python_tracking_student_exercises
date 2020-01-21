class Exercise:

    def __init__(self, name, language):
        self.exercise_name = name
        self.exercise_language = language

    def __str__(self):
        return f"{self.exercise_name}\n"