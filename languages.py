"""
CP1404 Prac07, "Intermediate Exercises" section
Client code for listing programming languages
Gareth Mullins, JCU student
Started 12/09/2016
"""

from Prac07.programmingLanguage import ProgrammingLanguage


def main():
    languages = [ProgrammingLanguage("Java", "Static", True, 1995),
                 ProgrammingLanguage("C++", "Static", False, 1983),
                 ProgrammingLanguage("Python", "Dynamic", True, 1991),
                 ProgrammingLanguage("Visual Basic", "Static", False, 1991),
                 ProgrammingLanguage("Ruby", "Dynamic", True, 1995)]

    for language in languages:
        print(str(language))

    print("\n" + "The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name())


if __name__ == "__main__":
        main()
