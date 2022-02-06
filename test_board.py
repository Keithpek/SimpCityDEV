from unittest import mock
from Board import *
from Menu import *
import builtins

def test_option_building():
    board = Board()
    # change as it will take in int instead of string
    for i in range (1, 8):
        with mock.patch.object(builtins, "input", lambda _: i):
            assert Option_Building(board) == i

    with mock.patch.object(builtins, "input", lambda _: "abc"):
        assert Option_Building(board) == "Wrong Input"

    with mock.patch.object(builtins, "input", lambda _: 0):
        assert Option_Building(board) == 0

    with mock.patch.object(builtins, "input", lambda _: 16):
        assert Option_Building(board) == "Out of Range"

def test_increase_turn():
    board = Board()
    result = board.turn + 1
    assert result == board.Next_Turn()

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


def test_change_buildingState():
    board = Board()

    if board.BuildingState[0] == "False":
        assert board.Change_BuildingState(1) == "True"
    elif board.BuildingState[0] == "True":
        assert board.Change_BuildingState(1) == "False"

    # -1 and below is out of range
    assert board.Change_BuildingState(-2) == "Out of Range"

    # 0 would return to main menu
    assert board.Change_BuildingState(0) == "Exitting"

    # 7 and above is out of range
    assert board.Change_BuildingState(7) == "Out of Range"

