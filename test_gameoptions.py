from Game_Options import building_choice, check_adjacent, place_building, prevent_overlap
from Menu import *
from Board import *
import pytest
    
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
