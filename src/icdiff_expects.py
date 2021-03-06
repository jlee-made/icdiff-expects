
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

__version__ = '0.0.1'

import pprint
import subprocess

from past.builtins import basestring

import expects
import icdiff_inprocess


class equal(expects.equal):

    nr_cols = 80

    def _failure_message(self, subject, *args):
        if isinstance(self._expected, basestring):
            expected = self._expected
        else:
            expected = pprint.pformat(self._expected)
        if isinstance(subject, basestring):
            got = subject
        else:
            got = pprint.pformat(subject)
        return icdiff_inprocess.diff_text(expected, got, nr_cols=self.nr_cols)


def diff(subject, expected, nr_cols=80):
    if isinstance(expected, basestring):
        expected_ = expected
    else:
        expected_ = pprint.pformat(expected)
    if isinstance(subject, basestring):
        got_ = subject
    else:
        got_ = pprint.pformat(subject)
    return icdiff_inprocess.diff_text(expected_, got_, nr_cols=nr_cols)


def print_diff(subject, expected, nr_cols=80):
    print(diff(subject, expected, nr_cols))
