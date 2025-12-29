from tkinter import messagebox
class Conditions(object):

    def check_letters(self, input_text: str, dict_letters: dict[str, int]) -> bool:
        for letter in input_text:
            if letter not in dict_letters:
                messagebox.showinfo("Incorrect letters", f"The letter {letter} is not allowed")
                return True
        return False

    def check_number_letters(self, input_text: str, list_unique_letters: list[str],
                             list_letters_3_times: list[str]) -> bool:
        frequency_dict = {}
        for letter in input_text:
            if letter in frequency_dict:
                frequency_dict.update({letter: frequency_dict[letter] + 1})
            else:
                frequency_dict.update({letter: 1})
        # check number of M:
        if "M" in frequency_dict and frequency_dict["M"] > 2:
            messagebox.showinfo("Too many M", "Just 2 M are allowed in a roman number")
            return True
        # check L, D, V:
        for un_letter in list_unique_letters:
            if un_letter in frequency_dict and frequency_dict[un_letter] > 1:
                messagebox.showinfo(f"Too many {un_letter}", f"Just 1 {un_letter} is allowed in a roman number")
                return True
        # check letters that can appear 3 times
        for letter in list_letters_3_times:
            if letter in frequency_dict and frequency_dict[letter] > 3:
                messagebox.showinfo(f"{letter} too often", f"Just 3 {letter} is allowed in a roman number")
                return True
        # special case of X xxxix
        if "X" in frequency_dict and frequency_dict["X"] > 3 and "XXXIX" not in input_text:
            messagebox.showinfo("Not permitted X combination", "4X are allowed just in combination XXXIX")
            return True
        return False

    def check_introduced_year(self, year_introduced: str) -> bool:
        year_int_introduced = int(year_introduced)
        if year_int_introduced <= 0 or year_int_introduced > 2500:
            messagebox.showinfo("Year not valid", "Please enter a year between 1 and 2500")
            return True
        return False

    def check_romanic_number(self, romanic_number: str, dict_values: dict[str, int],
                             allowed_pairs: dict[str, tuple[str, str]]) -> bool:
        dict_letter_index = {}
        for idx, letter in enumerate(romanic_number):
            dict_letter_index.setdefault(letter, []).append(idx)

        list_exceptions = []
        list_start_index_exceptions = []

        '''
        check if we have possible allowed combinations
        Basically we will have the now the last index of a letter so we need to check if the permitted combinations are index each other
        Allowed combinations:
            CM, CD, XC, XL, IX, IV
        If not check to see if we have this: M, D, C, X, L, V, I 
        '''
        for left, rights in allowed_pairs.items():
            if left not in dict_letter_index:
                continue
            for left_idx in dict_letter_index[left]:
                for right in rights:
                    if right not in dict_letter_index:
                        continue
                    for right_idx in dict_letter_index[right]:
                        if right_idx == left_idx + 1:
                            # Valid subtractive pair found
                            list_exceptions.append(dict_values[right] - dict_values[left])
                            list_start_index_exceptions.append(left_idx)
        '''check to see if we do not have letter values bigger
        need to check to not be in the exceptions, meaning
        CM, CD, XC, XL, IX, IV
        '''
        exception_positions = set(list_start_index_exceptions)
        # After building list_start_index_exceptions
        exception_positions = set(list_start_index_exceptions)

        i = 0
        while i < len(romanic_number):
            if i in exception_positions:
                # subtractive pair
                left = romanic_number[i]
                right = romanic_number[i + 1]
                pair_value = dict_values[right] - dict_values[left]

                # check next value after the pair
                if i + 2 < len(romanic_number):
                    next_value = dict_values[romanic_number[i + 2]]
                    if next_value >= pair_value:
                        messagebox.showinfo("Invalid number", f"{romanic_number} is not a valid roman number")
                        return True

                i += 2
            else:
                # normal descending rule
                if i + 1 < len(romanic_number):
                    if dict_values[romanic_number[i + 1]] > dict_values[romanic_number[i]]:
                        messagebox.showinfo("Invalid number", f"{romanic_number} is not a valid roman number")
                        return True
                i += 1

        return False
