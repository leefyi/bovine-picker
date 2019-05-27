#!/usr/local/bin python
# coding=utf-8
# @Time    : 2019-02-18 21:54
# @Author  : lifangyi
# @File    : picker.py
# @Software: PyCharm


class Picker(object):

    __slots__ = ['y', 'm', 'd', 'locale', 'description', '__name__', '__doc__']

    __week_dict = {
        'cn': (
            '星期日',
            '星期一',
            '星期二',
            '星期三',
            '星期四',
            '星期五',
            '星期六'
        ),
        'en': (
            'Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday'),
        'jp': (
            'にちようび',
            'げつようび',
            'かようび',
            'すいようび',
            'もくようび',
            'きんようび',
            'どようび'
        )}

    def __init__(self, locale=None):
        self.description = 'check out the day'
        if not locale:
            self.locale = 'en'
        else:
            self.locale = locale

    def what_day(self, birthay):
        index = self.getw(birthay)
        day_list = ['' for _ in range(7)]
        if self.locale == 'en':
            day_list = self.__week_dict['en']
        elif self.locale == 'cn':
            day_list = self.__week_dict['cn']
        elif self.locale == 'jp':
            day_list = self.__week_dict['jp']
        else:
            day_list = self.__week_dict['en']
        return day_list[index]

    def getw(self, birthday):
        self.birthday_formatter(birthday)

        year = int(self.y)
        month = int(self.m)
        day = int(self.d)

        if month < 3:
            year = year - 1
            month = month + 12

        c = year // 100
        year = year % 100

        w = year + year // 4 + c // 4 - 2 * \
            c + 26 * (month + 1) // 10 + day - 1
        return (w % 7 + 7) % 7

    def birthday_formatter(self, birthday):

        # supports 4 formats: yyyyMMdd, yyyy-MM-dd, yyyy/MM/dd, yyyy.MM.dd

        sb = str(birthday)
        if sb.strip() == '':
            raise Exception('birthday is null.')
        else:
            date = []
            # check the format then split
            if sb.count('-') > 0:
                date = sb.split('-')
                self.check_birth_items(date)
            elif sb.count('.') > 0:
                date = sb.split('.')
                self.check_birth_items(date)
            elif sb.count('/') > 0:
                date = sb.split('/')
                self.check_birth_items(date)
            else:
                if len(sb) > 8:
                    raise Exception('birthday too long.')
                year = sb[:4]
                month = sb[4:6]
                day = sb[6:]
                if year == '' or month == '' or day == '':
                    raise Exception('birthday too short.')
                date = [year, month, day]

            self.y = date[0]
            self.m = date[1]
            self.d = date[2]

    def check_birth_items(self, date):
        if len(date) < 3:
            if self.locale == 'en':
                raise Exception('birthday format is not valid.')
            elif self.locale == 'cn':
                raise Exception('生日格式不正确。')
            elif self.locale == 'jp':
                raise Exception('フォーマットが正しくない')
            else:
                raise Exception('birthday format is not valid.')
