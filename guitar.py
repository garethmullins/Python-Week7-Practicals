"""
CP1404 Prac07, "Do-from-scratch Exercises" section
Dynamically creates instances of guitars using the variables "name", "year" and "cost" and can calculate age's as of
    2016 and whether their vintages
Gareth Mullins, JCU student
Started 14/09/2016
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return "{:>{}} ({}), worth ${:10,.2f}".format(self.name, 20, self.year, self.cost)

    def get_age(self):
        """
        calculate the age of the guitar as of 2016
        """
        self.age = 2016 - self.year

    def is_vintage(self):
        """
        determine if the guitar is a vintage
        :return: if vintage: True, else: False
        """
        self.get_age()
        if self.age > 50:
            return True
        else:
            return False
