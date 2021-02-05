import unittest
from multiplicable_numbers import is_multiplicable


class TestMultiplicableValidations(unittest.TestCase):

    def setUp(self):
        self.all_from_one_to_a_hundred = [i for i in range(1, 101)]
        self.multiplicables_by_three = [i * 3 for i in range(1, 34)]
        self.multiplicables_by_five = [i * 5 for i in range(1, 21)]

    def test_true_multiplicables_by_three(self):
        self.results = [is_multiplicable(m, 3) for m in self.multiplicables_by_three]
        self.assertEqual(all(self.results), True)


if __name__ == '__main__':
    unittest.main()
