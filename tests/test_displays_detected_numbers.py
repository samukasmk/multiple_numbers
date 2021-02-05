import unittest
from multiplicable_numbers import displays_detected_numbers


class TestDisplaysDetectedNumbers(unittest.TestCase):

    def setUp(self):
        self.one_to_a_hundred_with_three_and_five_multiplicables = [
            '1', '2', 'Three', '4', 'Five', 'Three', '7', '8', 'Three', 'Five', '11', 'Three', '13', '14', 'ThreeFive',
            '16', '17', 'Three', '19', 'Five', 'Three', '22', '23', 'Three', 'Five', '26', 'Three', '28', '29',
            'ThreeFive', '31', '32', 'Three', '34', 'Five', 'Three', '37', '38', 'Three', 'Five', '41', 'Three', '43',
            '44', 'ThreeFive', '46', '47', 'Three', '49', 'Five', 'Three', '52', '53', 'Three', 'Five', '56', 'Three',
            '58', '59', 'ThreeFive', '61', '62', 'Three', '64', 'Five', 'Three', '67', '68', 'Three', 'Five', '71',
            'Three', '73', '74', 'ThreeFive', '76', '77', 'Three', '79', 'Five', 'Three', '82', '83', 'Three', 'Five',
            '86', 'Three', '88', '89', 'ThreeFive', '91', '92', 'Three', '94', 'Five', 'Three', '97', '98', 'Three',
            'Five']

        self.one_to_a_hundred_with_tow_and_four_multiplicables = [
            '1', 'Two', '3', 'TwoFour', '5', 'Two', '7', 'TwoFour', '9', 'Two', '11', 'TwoFour', '13', 'Two', '15',
            'TwoFour', '17', 'Two', '19', 'TwoFour', '21', 'Two', '23', 'TwoFour', '25', 'Two', '27', 'TwoFour', '29',
            'Two', '31', 'TwoFour', '33', 'Two', '35', 'TwoFour', '37', 'Two', '39', 'TwoFour', '41', 'Two', '43',
            'TwoFour', '45', 'Two', '47', 'TwoFour', '49', 'Two', '51', 'TwoFour', '53', 'Two', '55', 'TwoFour', '57',
            'Two', '59', 'TwoFour', '61', 'Two', '63', 'TwoFour', '65', 'Two', '67', 'TwoFour', '69', 'Two', '71',
            'TwoFour', '73', 'Two', '75', 'TwoFour', '77', 'Two', '79', 'TwoFour', '81', 'Two', '83', 'TwoFour', '85',
            'Two', '87', 'TwoFour', '89', 'Two', '91', 'TwoFour', '93', 'Two', '95', 'TwoFour', '97', 'Two', '99',
            'TwoFour']

        self.one_to_a_hundred_with_six_and_nine_multiplicables = [
            '1', '2', '3', '4', '5', 'Six', '7', '8', 'Nine', '10', '11', 'Six', '13', '14', '15', '16', '17',
            'SixNine', '19', '20', '21', '22', '23', 'Six', '25', '26', 'Nine', '28', '29', 'Six', '31', '32', '33',
            '34', '35', 'SixNine', '37', '38', '39', '40', '41', 'Six', '43', '44', 'Nine', '46', '47', 'Six', '49',
            '50', '51', '52', '53', 'SixNine', '55', '56', '57', '58', '59', 'Six', '61', '62', 'Nine', '64', '65',
            'Six', '67', '68', '69', '70', '71', 'SixNine', '73', '74', '75', '76', '77', 'Six', '79', '80', 'Nine',
            '82', '83', 'Six', '85', '86', '87', '88', '89', 'SixNine', '91', '92', '93', '94', '95', 'Six', '97', '98',
            'Nine', '100']

    def test_one_to_a_hundred_with_three_and_five_multiplicables(self):
        results = displays_detected_numbers(1, 100, [3, 5])
        self.assertEqual(results, self.one_to_a_hundred_with_three_and_five_multiplicables)

    def test_one_to_a_hundred_with_tow_and_four_multiplicables(self):
        results = displays_detected_numbers(1, 100, [2, 4])
        self.assertEqual(results, self.one_to_a_hundred_with_tow_and_four_multiplicables)

    def test_one_to_a_hundred_with_six_and_nine_multiplicables(self):
        results = displays_detected_numbers(1, 100, [6, 9])
        self.assertEqual(results, self.one_to_a_hundred_with_six_and_nine_multiplicables)
