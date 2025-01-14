# just some experiments

from dataclasses import dataclass
from typing import List
from CreateLayerClass import Layer
from CreatePageClass import Page
from CreateSquareClass import Square
from Configurations import *
from PlusMinusSquarePageAdditions import *



@dataclass
class Piece:
    name: str
    author: str
    default_settings: dict
    layers: List[Layer]
    nr_of_layers: int = 1

    def add_layer(self, layer: Layer):
        self.layers.append(layer)

    def create_piece(self):
        # how many of everything?
        nr_layers = int(input("nr of layers"))
        nr_pages = 7
        nr_squares = 4 # should be 52
        for n in range(nr_layers):
            # define page order
            page_order = define_default_pageorder() # function to get the default order for this layer
            # defined notepage order
            notepage_order = define_default_pageorder() # function to get the default order for this layer
            l = Layer(n+1,page_order,notepage_order,[])
            for m in range(nr_pages):
                pagenr = page_order[m]
                notepagenr = notepage_order[m]
                pas = page_arrow_statements[m] # source of the arrow statements, per page
                pts = page_tendency_statements[m] # source of the tendency change statements, per page
                p = Page(pagenr, notepagenr, pas, pts, [], [])
                for o in range(nr_squares):
                    sq = Square(o+1, "")  # TODO dit moet aangepast worden
                    # TODO nadenken hoe we square-data eerst kunnen ophalen, dan square mee definieren
                    p.add_square(sq)
                l.add_page(p)
            self.add_layer(l)



# generate random squares - for testing purposes
'''
s1 = Square(1, " blabla")

s2 = Square(2, "deep")

p1 = Page(1, 2, {}, {}, [4,5,6], [])
p1.add_square(s1)
p1.add_square(s2)

l1 = Layer(1, [], [],[])
l1.add_page(p1)
l2 = Layer(2, [], [], [])
l2.add_page(p1)
'''

piece1 = Piece("eerste","me",{},[])
#piece1.add_layer(l1)
#piece1.add_layer(l2)
piece1.create_piece()

print(piece1)

'''for l in piece1.layers:
    print(l.layer_nr)
    for p in l.pages:
        print(p.pagenr)
        for sq in p.squares:
            print(sq)
'''


# bij wijze van test een hele Square
# neem square 40 van symbolpage 1
# 1, 1,42,40,0,0,6,0,3,2,0,2,0,2,0,1,6,8,0,0,6,0,0,3,1,7
# pas op: layernr toegevoegd als 1e nummer
# square1_40 = Square(1, 1,42,40,0,0,6,0,3,2,0,2,0,2,0,1,6,8,0,0,6,0,0,3,1,7)
square1_40 = Square(1, 1,42,40,0,0,6,0,3,0,0,2,0,2,3,1,6,8,0,0,6,0,0,3,1,7)

square1_40.print_square()
square1_40.set_notepagenr(1)

seq = square1_40.make_sequence()
print(f" accidents: {seq[0]}")
print(f" central sound: {seq[1]}")
print(f" subsidiaries {seq[2]}")

#print(seq)

# om de sequence te bepalen, moet
# 1. eerst de configuratie worden opgehaald om de matchende notepage te vinden. Import Configurations.py, functie get_config1()
# 2. de notepage moet worden opgehaald, aan de hand van de symbolpage
# 3. de notepage moet worden geparsed om de chord en melody te bepalen

