# coding = utf-8
# author:lifangyi
# date: 2019/5/24 09:52:00
# file: picker_test.py

import unittest
from picker import Picker

# unit test
# travis


class PickerTestCase(unittest.TestCase):

    def setUp(self):
        self.picker = Picker()
        print('picker unit test start.')

    def tearDown(self):
        del self.picker
        print('picker unit test end.')

    def test_check_birth_items(self):
        sample_date = '2000'
        tag = self.picker.check_birth_items(sample_date)
        self.assertEqual(tag, None, 'wrong type check')

    def test_birthday_formatter(self):
        date = '1990-11-25'
        self.picker.birthday_formatter(date)
        self.assertEqual(self.picker.y, '1990', 'wrong year after parser')
        self.assertEqual(self.picker.m, '11', 'wrong month after parser')
        self.assertEqual(self.picker.d, '25', 'wrong day after parser')

    def test_what_day(self):
        date = '1990-11-25'
        wd = self.picker.what_day(date)
        self.assertEqual(wd, 'Sunday', 'not a good calculation')


if __name__ == '__main__':
    unittest.main()