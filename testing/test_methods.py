import time
import unittest

from logic.initializer import Initializer
from logic.conditioner import Conditions
from logic.calculator import Calculate

class TestMethods(unittest.TestCase):

    @classmethod
    def setUp(self):
        #we will create at the beginning 3 instances
        self.initializer = Initializer()
        self.conditions = Conditions()
        self.calculator = Calculate()
        print("Starting tests")
        time.sleep(2)

    @classmethod
    def tearDown(self):
        print("Finished tests")

    def test_number_romanic_false(self):
        romanic_number = "MMCCMCDXXVIII"
        result = self.initializer.introduce_roman_number(romanic_number)
        #create the test
        self.assertEqual(result, "Error")

    def test_number_romanic_true(self):
        romanic_number = "MMCCLXXVIII"
        result = self.initializer.introduce_roman_number(romanic_number)
        self.assertEqual(result, romanic_number)

    def test_number_arabic_false1(self):
        arabic_number = "MX"
        #for assert raises we need to first appeal the exception assert using with and appeal then the function, result
        with self.assertRaises(ValueError, msg="Needs to be a number"):
            result = self.initializer.introduce_year(arabic_number)

    def test_number_arabic_false2(self):
        arabic_number = "3000"
        result = self.initializer.introduce_year(arabic_number)
        self.assertEqual(result, 0)

    def test_number_arabic_true(self):
        arabic_number = 1947
        result = self.initializer.introduce_year(arabic_number)
        self.assertEqual(result, arabic_number)

    ''''
    converting tests
    '''
    def test_romanic_decimal_conversion(self):
        #valid romanic number
        romanic_number = "mdcclxxix"
        result = self.calculator.convert_romanic_number(romanic_number) #1779\
        self.assertEqual(result, (romanic_number.upper(),1779), msg="Romanic number should be 1779")

    def test_decimal_romanic_conversion(self):
        #valid decimal number
        arabic_number = 1779
        result = self.calculator.convert_decimal_number(arabic_number)#MDCCLXXIX
        self.assertEqual(result, (str(arabic_number),"MDCCLXXIX"), msg="Romanic number should be MDCCLXXIX")




