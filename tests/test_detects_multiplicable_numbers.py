import unittest
from multiplicable_numbers import detects_multiplicable_numbers


class TestDetectsMultiplicableNumbers(unittest.TestCase):

    def setUp(self):
        self.multiplicables_by_three = {i * 3 for i in range(1, 34)}
        self.multiplicables_by_five = {i * 5 for i in range(1, 21)}
        self.multiplicables_by_three_and_five = self.multiplicables_by_three & self.multiplicables_by_five
        self.multiplicables_just_by_three = self.multiplicables_by_three - self.multiplicables_by_three_and_five
        self.multiplicables_just_by_five = self.multiplicables_by_five - self.multiplicables_by_three_and_five

        self.all_from_one_to_a_hundred = {i for i in range(1, 101)}
        self.non_multiplicables_by_three = self.all_from_one_to_a_hundred - self.multiplicables_by_three
        self.non_multiplicables_by_five = self.all_from_one_to_a_hundred - self.multiplicables_by_five
        self.non_multiplicables_by_three_or_five = self.all_from_one_to_a_hundred - (
                self.multiplicables_by_three | self.multiplicables_by_five)

    def test_multiplicables_just_by_three(self):
        results = [detects_multiplicable_numbers(m, [3]) == 'Three' for m in self.multiplicables_just_by_three]
        self.assertEqual(all(results), True)

    def test_multiplicables_just_by_five(self):
        results = [detects_multiplicable_numbers(m, [5]) == 'Five' for m in self.multiplicables_just_by_five]
        self.assertEqual(all(results), True)

    def test_multiplicables_by_three_and_five(self):
        results = [detects_multiplicable_numbers(m, [3, 5]) == 'ThreeFive' for m in self.multiplicables_by_three_and_five]
        self.assertEqual(all(results), True)

    def test_non_multiplicables_by_three(self):
        results = [detects_multiplicable_numbers(m, [3]) == str(m) for m in self.non_multiplicables_by_three]
        self.assertEqual(all(results), True)

    def test_non_multiplicables_by_five(self):
        results = [detects_multiplicable_numbers(m, [5]) == str(m) for m in self.non_multiplicables_by_five]
        self.assertEqual(all(results), True)

    def test_non_multiplicables_by_three_five(self):
        results = [detects_multiplicable_numbers(m, [3, 5]) == str(m) for m in self.non_multiplicables_by_three_or_five]
        self.assertEqual(all(results), True)
