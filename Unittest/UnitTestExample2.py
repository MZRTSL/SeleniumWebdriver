import unittest


class MyTestCase(unittest.TestCase):
    def test_addNumber(self):
        print(2+3)
        self.assertEqual(2,2)

    def test_subNumber(self):
        print(5-2)


