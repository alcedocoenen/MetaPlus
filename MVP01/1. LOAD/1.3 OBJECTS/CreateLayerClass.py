
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

    def set_pageorder(self, order = [1,2,3,4,5,6,7]):
        # meant to enter an alternative order
        self.page_order = order

    def set_notepageorder(self, order = [1,2,3,4,5,6,7]):
        # meant to enter an alternative order
        self.notepage_order = order

