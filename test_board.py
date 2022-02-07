from unittest import mock

import pytest
from Board import *
from Menu import *
import builtins

def test_increase_turn():
    board = Board()
    result = board.turn + 1
    assert result == board.Next_Turn()
'''
    value > output
    PASSING UNIT TEST
    == Range from 0 to data size ==
        o buildingState 1 > data item 1
        0 buildingState 2 > data item 2
        o ...
        o buildingState n > data item n
'''
def test_get_buildingState():
    board = Board()

    adds_line = "/q"
    adds_line = adds_line.replace("q", "")

    path = str(pathlib.Path(__file__).parent.resolve()) + "/.." + adds_line + "data/state_data.txt"

    txt_data = open(path,"r")
    sv_data = txt_data.readline()
    sv_data = sv_data.split(";")

    for i in range(0, len(sv_data)):
        assert board.Get_BuildingState()[i] == sv_data[i]


'''
    value > output
    FAILING UNIT TEST
        o -2 > "Out of Range"
        o 0 > "Exitting"
        o 8 > "Out of Range"

    value > output [true result]
    SKIP UNIT TEST
        o 1 > "Out of Range"    [1 > 1]
        o 8 > 8                 [8 > "Out of Range"]
'''
@pytest.mark.parametrize("value, output", 
                        [
                            (-2, "Out of Range"), 
                            (0, "Exitting"), 
                            (8, "Out of Range"), 
                            pytest.param(1, "Out of Range", marks=pytest.mark.xfail), 
                            pytest.param(1, "Exitting", marks=pytest.mark.xfail)
                            ])
def test_change_buildingState_failing(value, output):
    board = Board()

    # -1 and below is out of range
    # 0 would return to main menu
    # 7 and above is out of range
    assert board.Change_BuildingState(value) == output

'''
    value > output : output2
    PASSING UNIT TEST
        o 0 > "True" : "False"
        o 1 > "True" : "False"
        o ...
        o 7 > "True" : "False"
'''
@pytest.mark.parametrize("value, output, output2", 
                            [
                                (1, "True", "False"), 
                                (2, "True", "False"), 
                                (3, "True", "False"),
                                (4, "True", "False"),
                                (5, "True", "False"),
                                (6, "True", "False"),
                                (7, "True", "False")
                            ])
def test_change_buildingState_passing(value, output, output2):
    board = Board()
    # when called board.Change_BuildingSate(output) it will become the opposite of what it is
    # "true" becomes "false"
    # "false" becomes "true"
    # testing is done to see if changing it once will turn it to True then calling the function again would turn it to False
    assert board.Change_BuildingState(value) == output

    assert board.Change_BuildingState(value) == output2