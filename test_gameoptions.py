from Game_Options import *
from Menu import *
from Board import *
import pytest
from unittest import mock
    
def test_invalid_col():
    board=Board()
    checkboard=board.New_Board()
    result=place_building(board,"HSE","F1")
    assert result=="Invalid col"

    
def test_invalid_row():
    board=Board()
    checkboard=board.New_Board()
    result=place_building(board,"HSE","A5")
    assert result=="Invalid row"

    
def test_invalid_opt():
    board=Board()
    checkboard=board.New_Board()
    result=place_building(board,"HSE","A2B")
    assert result=="Invalid opt"

    
def test_overlap():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A2","HSE")
    result=prevent_overlap(board,"A2","PRK")
    assert result=="Overlap"

    
def test_no_adjacent():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A2","HSE")
    result=check_adjacent(board,"C1","HSE")
    assert result=="No adjacent"

    
def test_adjacent():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A2","HSE")
    result=check_adjacent(board,"A3","HSE")
    assert result=="Have adjacent"

    
def test_first_turn():
    board=Board()
    checkboard=board.New_Board()
    result=check_adjacent(board,"A2","HSE")
    assert result=="Turn 1"


def test_built():
    board=Board()
    checkboard=board.New_Board()
    result=building_choice(board,"A2", "HSE")
    assert result=="Successfully built"

def test_modify_highscore():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A1","MON")
    building_choice(board,"B1","PRK")
    building_choice(board,"C1","MON")
    building_choice(board,"D1","MON")
    building_choice(board,"A2","PRK")
    building_choice(board,"B2","PRK")
    building_choice(board,"C2","PRK")
    building_choice(board,"D2","PRK")
    building_choice(board,"A3","HWY")
    building_choice(board,"B3","HWY")
    building_choice(board,"C3","HWY")
    building_choice(board,"D3","HWY")
    building_choice(board,"A4","MON")
    building_choice(board,"B4","MON")
    building_choice(board,"C4","MON")
    building_choice(board,"D4","MON")
    with mock.patch('builtins.input', return_value="Testname"):
        assert Verify_Modify_highscore(board) == "Modified highscore"

def test_no_highscore():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A1","FAC")
    building_choice(board,"B1","FAC")
    building_choice(board,"C1","FAC")
    building_choice(board,"D1","FAC")
    building_choice(board,"A2","FAC")
    building_choice(board,"B2","FAC")
    building_choice(board,"C2","FAC")
    building_choice(board,"D2","FAC")
    building_choice(board,"A3","FAC")
    building_choice(board,"B3","FAC")
    building_choice(board,"C3","FAC")
    building_choice(board,"D3","FAC")
    building_choice(board,"A4","FAC")
    building_choice(board,"B4","FAC")
    building_choice(board,"C4","FAC")
    building_choice(board,"D4","FAC")
    result = Verify_Modify_highscore(board)
    assert result=="No highscore"

def test_view_highscore():
    result=View_highscore()
    assert result==True
