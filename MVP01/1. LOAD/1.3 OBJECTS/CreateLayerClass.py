
from dataclasses import dataclass
from typing import List

from CreatePageClass import Page


@dataclass
class Layer:
    layer_nr: int
    page_order: list
    notepage_order: list
    pages: List[Page]

    def add_page(self, page: Page):
        self.pages.append(page)
