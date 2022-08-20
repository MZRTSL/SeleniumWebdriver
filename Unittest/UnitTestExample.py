import unittest
from DemoExample1 import TestCase1
# I created two class with 2 methods inside that and I created a unittest in which I called this 2 methods

class MyTestCase(unittest.TestCase):
    def test_adding_numbers(self):
        TestCase1.add(self, 3, 5)

    def test_sub_numbers(self):
        TestCase1.sub(self, 5, 2)

# if __name__ == '__main__':
#     unittest.main()
