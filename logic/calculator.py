from logic.initializer import Initializer
class Calculate(object):

    def __init__(self):
        self.initializer = Initializer()

    @staticmethod
    def get_digits_number(year:int)->list[int]:
        list_digits = []
        while int(year) !=0:
            digit = year % 10
            list_digits.append(digit)
            year = year //10
        return list_digits[::-1]

    def invert_dictionary(self) ->dict[int, str]:
        inverted_dict = {}
        for key, value in self.initializer.dict_letters.items():
            inverted_dict.update({value:key})
        return inverted_dict


    def convert_decimal_number(self, introduced_year:int) ->tuple[str, str]:
        inverted_dict = self.invert_dictionary()
        roman_number = ""
        '''
        We will need to see how many digits we have
        Based on the digits we will determine how to calculate the number 
        '''
        introduced_year = self.initializer.introduce_year(introduced_year)
        if introduced_year == 0:
            return None
        list_years = self.get_digits_number(introduced_year)
        if len(list_years) == 4:
            for i in range (0, len(list_years)):
                if i ==0:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[1000]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[1000]
                if i ==1:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[100]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[100]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[100]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[100] + inverted_dict[500]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[500]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[500] + inverted_dict[100]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[500] + 2 * inverted_dict[100]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[500] + 3 * inverted_dict[100]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[100] + inverted_dict[1000]
                if i == 2:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[10]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[10]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[10]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[10] + inverted_dict[50]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[50]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[50] + inverted_dict[10]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[50] + 2 * inverted_dict[10]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[50] + 3 * inverted_dict[10]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[10] + inverted_dict[100]
                if i == 3:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[1]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[1]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[1]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[1] + inverted_dict[5]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[5]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[5] + inverted_dict[1]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[5] + 2 * inverted_dict[1]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[5] + 3 * inverted_dict[1]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[1] + inverted_dict[10]
        if len(list_years) == 3:
            for i in range(0, len(list_years)):
                if i == 0:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[100]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[100]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[100]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[100] + inverted_dict[500]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[500]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[500] + inverted_dict[100]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[500] + 2 * inverted_dict[100]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[500] + 3 * inverted_dict[100]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[100] + inverted_dict[1000]
                if i == 1:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[10]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[10]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[10]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[10] + inverted_dict[50]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[50]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[50] + inverted_dict[10]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[50] + 2 * inverted_dict[10]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[50] + 3 * inverted_dict[10]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[10] + inverted_dict[100]
                if i == 2:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[1]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[1]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[1]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[1] + inverted_dict[5]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[5]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[5] + inverted_dict[1]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[5] + 2 * inverted_dict[1]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[5] + 3 * inverted_dict[1]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[1] + inverted_dict[10]
        if len(list_years) == 2:
            for i in range(0, len(list_years)):
                if i == 0:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[10]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[10]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[10]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[10] + inverted_dict[50]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[50]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[50] + inverted_dict[10]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[50] + 2 * inverted_dict[10]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[50] + 3 * inverted_dict[10]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[10] + inverted_dict[100]
                if i == 1:
                    if list_years[i] == 1:
                        roman_number += inverted_dict[1]
                    elif list_years[i] == 2:
                        roman_number += 2 * inverted_dict[1]
                    elif list_years[i] == 3:
                        roman_number += 3 * inverted_dict[1]
                    elif list_years[i] == 4:
                        roman_number += inverted_dict[1] + inverted_dict[5]
                    elif list_years[i] == 5:
                        roman_number += inverted_dict[5]
                    elif list_years[i] == 6:
                        roman_number += inverted_dict[5] + inverted_dict[1]
                    elif list_years[i] == 7:
                        roman_number += inverted_dict[5] + 2 * inverted_dict[1]
                    elif list_years[i] == 8:
                        roman_number += inverted_dict[5] + 3 * inverted_dict[1]
                    elif list_years[i] == 9:
                        roman_number += inverted_dict[1] + inverted_dict[10]
        if len(list_years) ==1:
            if list_years[0] == 1:
                roman_number += inverted_dict[1]
            elif list_years[0] == 2:
                roman_number += 2 * inverted_dict[1]
            elif list_years[0] == 3:
                roman_number += 3 * inverted_dict[1]
            elif list_years[0] == 4:
                roman_number += inverted_dict[1] + inverted_dict[5]
            elif list_years[0] == 5:
                roman_number += inverted_dict[5]
            elif list_years[0] == 6:
                roman_number += inverted_dict[5] + inverted_dict[1]
            elif list_years[0] == 7:
                roman_number += inverted_dict[5] + 2 * inverted_dict[1]
            elif list_years[0] == 8:
                roman_number += inverted_dict[5] + 3 * inverted_dict[1]
            elif list_years[0] == 9:
                roman_number += inverted_dict[1] + inverted_dict[10]
        year_introduced = "".join(map(str, list_years))
        return year_introduced,  roman_number

    def convert_romanic_number(self, introduced_roman_number: str) -> tuple[str, int]:
        number_int = 0
        introduced_roman_number = self.initializer.introduce_roman_number(introduced_roman_number)
        if introduced_roman_number == "Error":
            return None
        # TO NOT GET INDEX OUT OF RANGE
        introduced_roman_number_spaced = introduced_roman_number +"n"
        '''
        We need to have some corner cases in which we need to check if we have for example:
        CM = 900 , CD = 400, XC=90,  XL =40, IX=9,  IV =4 
        In this case we need to count 2 letters
        '''
        counter = 0
        while counter <= len(introduced_roman_number_spaced)-1:
            #900
            if introduced_roman_number_spaced[counter] == "C" and introduced_roman_number_spaced[counter + 1] == "M":
                number_int +=self.initializer.dict_letters["M"] - self.initializer.dict_letters["C"]
                counter+=2
            #400
            elif introduced_roman_number_spaced[counter] == "C" and introduced_roman_number_spaced[counter + 1] == "D":
                number_int +=self.initializer.dict_letters["D"] - self.initializer.dict_letters["C"]
                counter+=2
            #90
            elif introduced_roman_number_spaced[counter] == "X" and introduced_roman_number_spaced[counter+1] =="C":
                number_int += self.initializer.dict_letters["C"] - self.initializer.dict_letters["X"]
                counter+=2
            #40
            elif introduced_roman_number_spaced[counter] =="X" and introduced_roman_number_spaced[counter+1] =="L":
                number_int += self.initializer.dict_letters["L"] - self.initializer.dict_letters["X"]
                counter+=2
            #9
            elif introduced_roman_number_spaced[counter] =="I" and introduced_roman_number_spaced[counter+1] =="X":
                number_int += self.initializer.dict_letters["X"] - self.initializer.dict_letters["I"]
                counter+=2
            #4
            elif introduced_roman_number_spaced[counter] =="I" and introduced_roman_number_spaced[counter+1] == "V":
                number_int += self.initializer.dict_letters["V"] - self.initializer.dict_letters["I"]
                counter+=2
            else:
                number_int += self.initializer.dict_letters[introduced_roman_number_spaced[counter]]
                counter+=1
        return introduced_roman_number, number_int






