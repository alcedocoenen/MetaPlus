
from dataclasses import dataclass
from typing import List
from CreateSquareClass import Square

@dataclass
class Page:
    pagenr: int
    symbolpagenr: int
    changes: dict
    exchange_instructions: dict
    empty_squares: list
    squares: List[Square]

    def add_square(self, square: Square):
        self.squares.append(square)