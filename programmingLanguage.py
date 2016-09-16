"""
CP1404 Prac07, "Intermediate Exercises" section
Dynamically creates instances of programming languages using the variables "name", "typing", "reflection" and "year"
Gareth Mullins, JCU student
Started 12/09/2016
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{:15} {:15} {:17} First appeared in {:4}".format(self.name + ",", self.typing + " Typing,",
                                                        "Reflection=True," if self.reflection else "Reflection=False,",
                                                                 self.year)

    def name(self):
        return self.name

    def is_dynamic(self):
        """
        check if typing is dynamic
        :return: boolean
        """
        if self.typing == "Dynamic":
            return True
        else:
            return False
