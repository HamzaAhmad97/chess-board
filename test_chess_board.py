import pytest
from chess_board import ChessBoard

@pytest.fixture
def board():
    return ChessBoard()

@pytest.mark.parametrize(
    "red, blue, under_attack",
    [
        ([1,3],[1,6],True),
        ([2,4],[4,2],True),
        ([2,5],[6,5],True),
        ([3,2],[1,5],False),
        ([6,1],[4,4],False),
        ([1,1],[2,2],True),
    ],
)
def test_is_under_attack(red, blue, under_attack, board):
    board.add_red(*red)
    board.add_blue(*blue)
    assert board.is_under_attack() == under_attack