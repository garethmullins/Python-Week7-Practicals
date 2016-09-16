"""
CP1404/CP5632 Practical
Car class example
Started 10/09/2016
"""

class Car:
    def __init__(self, name='', fuel=0, odometer=0):
        """ initialise a Car instance
        fuel: float, one unit of fuel drives one kilometre """
        self.fuel = fuel
        self.odometer = odometer
        self.name = name

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """
        add amount to the car's fuel
        :param amount: number of fuel units
        :return: None
        """
        self.fuel += amount

    def drive(self, distance):
        """
        drive the car a given distance if it has enough fuel
        or drive until fuel runs out
        :param distance:
        :return: None
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
