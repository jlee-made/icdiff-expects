from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
# import re

from expects import contain, equal, expect
from expects.testing import failure
import icdiff_expects


# TODO: use this (need ANOTHER matcher to test icdiff_expects.equal, because
# otherwise expects.testing.failure doesn't give you access to the result to
# equal)

# class Terminal(object):

#     # _xterm_color_regexp = re.compile('\033[[]38;5;([0-9;]*)m')
#     # _color_regexp = re.compile('\033[[]([0-9;]*)m')
#     _color_regexp = re.compile('\x1b[[](0-9;]*)m')
#     _colors = {'0': 'normal', '1': 'bold', '30': 'black', '31': 'red',
#                '32': 'green', '33': 'yellow', '34': 'blue',
#                '35': 'magenta', '36': 'cyan', '37': 'grey'}

#     def to_markup(self, text):
#         # if "\033[38;5;" in text:
#         #     text = self._xterm_color_regexp.sub(self._xterm_color, text)
#         if ('\x1b' + '[') in text:
#             text = self._color_regexp.sub(self._color, text)
#         return text

#     def _xterm_color(self, match):
#         return "{xterm %s}" % match.group(1)

#     def _color(self, match):
#         colorstring = '{'
#         for number in match.group(1).split(';'):
#             colorstring += self._colors.get(number, '?')
#         return colorstring + '}'


class Test(TestCase):

    def test(self):
#         expect_diff = '''\
# expected                                got
# {'spam_code': 'spam',                   {'spam_code': 'spam',
#  'spam_count': 4295,
#  'spam_id': '32102903',                  'spam_id': '32102903',
#  'spam_method': 'thorough',              'spam_method': 'thorough',
#  'spam_transaction': 'ABS32402983SAJFD   'spam_transaction': 'ABS32402983SAJFD
# AJFS',                                  AJFS',
#  'spam_type': 'full',                    'spam_type': 'full',
#  'spamspamspamspam': '2016-08-26T15:20   'spamspamspamspam': '2016-08-26T15:21
# :12Z'}                                  :12Z'}

# '''
        expect_value = {
            "spam_id": "32102903",
            "spam_code": "spam",
            "spam_count": 4295,
            "spam_method": "thorough",
            "spam_type": "full",
            "spamspamspamspam": "2016-08-26T15:20:12Z",
            "spam_transaction": "ABS32402983SAJFDAJFS"
        }
        got_value = {
            "spam_id": "32102903",
            "spam_code": "spam",
            "spam_method": "thorough",
            "spam_type": "full",
            "spamspamspamspam": "2016-08-26T15:21:12Z",
            "spam_transaction": "ABS32402983SAJFDAJFS"
        }
        expect_snippet = ("'spamspamspamspam': '2016-08-26T15:2\x1b[0;33m1\x1b[m \n\x1b[0;33m\x1b[m:12Z'}")
        with failure(contain(expect_snippet)):
            expect(got_value).to(icdiff_expects.equal(expect_value))
