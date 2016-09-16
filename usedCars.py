"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
Started 10/09/2016
"""

from Prac07.car import Car


def main():
    cars = [Car("Bus", 180, 0),
            Car("Limo", 100, 0)]

    # Limo
    cars[1].add_fuel(20)
    print("Fuel =", cars[1].fuel)
    cars[1].drive(115)
    print("Odometer =", cars[1].odometer)

    # Bus
    cars[0].drive(30)
    print("Fuel =", cars[0].fuel)
    print("Odometer =", cars[0].odometer)

    print([str(car) for car in cars])


if __name__ == "__main__":
        main()
