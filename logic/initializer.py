from tkinter import messagebox

from logic.conditioner import Conditions


class Initializer:

    def __init__(self):
        self.dict_letters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            # to not get out of range at calculation
            "n": 0

        }
        # Allowed subtractive pairs subtractive = { 'I': ('V', 'X'), 'X': ('L', 'C'), 'C': ('D', 'M') }
        self.subtractive = {
            'I': ('V', 'X'),
            'X': ('L', 'C'),
            'C': ('D', 'M')
        }
        self.unique_letters = ["V", "L", "D"]
        self.three_time_letters = ["I", "C"]
        self.conditions = Conditions()

    def introduce_year(self, introduced_year) -> int:
        if self.conditions.check_introduced_year(introduced_year):
            return 0
        return int(introduced_year)

    def introduce_roman_number(self, introduced_roman_number: str):
        introduced_roman_number = introduced_roman_number.upper()
        # start the checks
        if self.conditions.check_letters(introduced_roman_number, self.dict_letters):
            return "Error"
        if self.conditions.check_number_letters(introduced_roman_number, self.unique_letters,  self.three_time_letters):
            return "Error"
        if self.conditions.check_romanic_number(introduced_roman_number, self.dict_letters, self.subtractive):
            return "Error"
        return introduced_roman_number
