
from dataclasses import dataclass
from typing import List
from CreateSquareClass import Square

@dataclass
class Page:
    pagenr: int
    notepagenr: int
    page_arrows_instructions: list
    page_tendency_instructions: list
    empty_squares: list
    squares: List[Square]

    def add_square(self, square: Square):
        self.squares.append(square)