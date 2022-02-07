from unittest import mock

import pytest
from Board import *
from Menu import *
import builtins

'''
    value > output
    FAILING UNIT TEST
        o "abc" > "Wrong Input"
        o "1abs" > "Wrong Input"
        o 16 > "Out of Range"
        o -1 > "Out of Range"

    value > output [true result]
    SKIP UNIT TEST
        o 1 > "Out of Range"    [1 > 1]
        o 8 > 8                 [8 > "Out of Range"]
'''

@pytest.mark.parametrize("value, output",
                        [
                            ("abc", "Wrong Input"), 
                            (16, "Out of Range"),
                            ("a1", "Wrong Input"),
                            ("1abs", "Wrong Input"),
                            (-1, "Out of Range"),
                            pytest.param(1, "Out of Range", marks=pytest.mark.xfail), 
                            pytest.param(9, 9, marks=pytest.mark.xfail)
                            ])
def test_option_building_failing(value, output):
    board = Board()

    with mock.patch.object(builtins, "input", lambda _: value):
        assert Option_Building(board) == output

'''
    value > output
    PASSING UNIT TEST
    == Range from 1 to 7 ==
        o 0 > 0
        0 1 > 1
        o ...
        o 7 > 7
'''
def test_option_building_passingRange():
    board = Board()

    # change as it will take in int instead of string
    for i in range (1, 8):
        with mock.patch.object(builtins, "input", lambda _: i):
            assert Option_Building(board) == i