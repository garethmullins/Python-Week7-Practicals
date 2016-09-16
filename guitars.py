"""
CP1404 Prac07, "Do-from-scratch Exercises" section
Client code for getting and listing the user's guitars with their "name", "year" of construction and "cost"
Gareth Mullins, JCU student
Started 14/09/2016
"""

from Prac07.guitar import Guitar


def main():
    guitar_number = 0
    guitars = menu()

    # print "... snip ..." in the center of 64 characters
    print("\n" + "{:^64}".format("... snip ...") + "\n")

    print("These are my guitars:")
    for guitar in guitars:
        guitar_number += 1
        # print the guitar details and if it's a vintage guitar
        print("Guitar {}: {} {}".format(guitar_number, str(guitar), "(vintage)" if guitar.is_vintage() else ""))


def menu():
    """
    get details for each of the user's guitars (until the user gives an empty string for the name)
    :return: guitars
    """
    guitars = []

    # get the guitar details (name, year of production and cost) with error checking untill an empty input is given for
    #   the guitar name
    name = input("Name: ")
    while name != "".strip():
        year_is_valid = False
        cost_is_valid = False
        while year_is_valid is False:
            year = input("Year: ")
            if year_check(year):
                year_is_valid = True
            else:
                print("Invalid input, year must be a whole number with no letters")
        while cost_is_valid is False:
            cost = input("Cost: $")
            if float_check(cost):
                cost_is_valid = True
                cost = float(cost)
            else:
                print("Invalid input, cost must consist of numbers, no letters or symbols")

        # append error checked guitar details
        guitars.append(Guitar(name, year, cost))

        print("{} ({}) : ${:,.2f} added.".format(name, year, cost))
        # get name for the next loop (or to finish looping)
        name = input("Name: ")

    return guitars


def year_check(year):
    # try to make check_year equal to the int version of year, if that can't be done, the except ValueError triggers and
    #   False is returned
    try:
        check_year = int(year)
        # if year is empty then False is returned
        if year != "".strip():
            return True
        else:
            return False
    except ValueError:
        return False


def float_check(value):
    # try to make check_float equal to the float version of value, if that can't be done, the except ValueError triggers
    #   and False is returned
    try:
        check_float = float(value)
        # if value is empty then False is returned
        if value != "".strip():
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
        main()
