# config.py
# this file is meant to collect all setup and config parameters
# instead of using a GUI for asking.
# later this can be replaced by a genuine GUI that reads and writes confi files.

import PlusMinusSquarePageAdditions as page_instr
import random


# ============== CONFIG 0a ====================
# config 0a is about replacing the 4-tendencies with one of them
# re: rule 20 in the instructions.

config0a_a = "random once defined"
config0a_b = "random per case"
config0a_c = "increase"
config0a_d = "decrease"

def getconfig0():
    return config0a_b

#=============== CONFIG 1 =====================
# Config1 is about the number of layers and the order or pages.

config1a = {
                1:
                     {"layernr" : 1,
                      "order of squarepages": [3, 5, 2, 4, 1, 6, 7],
                      "order of notepages": [4, 5, 6, 7, 3, 2, 1]
                      },
                2:
                     {"layernr" : 2,
                      "order of squarepages": [6, 7, 2, 4, 1, 3, 5],
                      "order of notepages": [4, 5, 6, 7, 3, 2, 1]
                      }
}

config1b = {
                1:
                     {"layernr" : 1,
                      "order of squarepages": [1, 2, 3, 4, 5, 6, 7],
                      "order of notepages": [1, 2, 3, 4, 5, 6, 7]
                      },
                2:
                     {"layernr" : 2,
                      "order of squarepages": [3, 5, 2, 4, 1, 6, 7],
                      "order of notepages": [4, 5, 6, 7, 3, 2, 1]
                      },
                3:
                    {"layernr": 3,
                     "order of squarepages": [7, 6, 5, 4, 3, 2, 1],
                     "order of notepages": [1, 2, 3, 4, 5, 6, 7]
                     },
}

config1c = {
                1:
                     {"layernr" : 1,
                      "order of squarepages": [1, 2, 3, 4, 5, 6, 7],
                      "order of notepages": [1, 2, 3, 4, 5, 6, 7]
                      }
}

# TODO define a function for defining the config1 dynamically (random)
# here is the main variable. Change this when choosing another configuration
def get_config1():
    return config1a
def get_order_of_squarepages(layer):
    return get_config1()[layer]['order of squarepages']

def get_order_of_notepages(layer):
    return get_config1()[layer]['order of notepages']


def get_number_of_layers():
    return len(get_config1())

#test
#print(get_order_of_squarepages(1))
#print(get_order_of_notepages(1))


#=============== CONFIG 2 =====================
# Config2 is about square substitution



# some sample tuple lists to be used:
config2a = [(2, 27, 7), (2, 28, 14), (3, 39, 7), (3, 41, 7), (5, 33, 7), (5, 24, 7), (6, 44, 12), (6, 23, 12)]
config2b = [(3, 39, 7), (3, 8, 7), (3, 41, 7), (3, 13, 7), (4, 17, 14), (4, 51, 14), (6, 47, 9), (6, 44, 12), (7, 49, 7)]
config2c = [(2, 47, 7), (2, 49, 14), (3, 13, 7), (3, 8, 7), (3, 39, 7), (5, 33, 7), (7, 41, 7)]
config2d = [(3, 8, 7), (3, 39, 7), (4, 11, 14), (4, 5, 14), (5, 49, 7), (5, 46, 7), (6, 47, 9), (6, 46, 12), (7, 36, 7)]

def make_choices_for_tendency_substitutes(instructions = page_instr.page_tendency_statements):
    # in this function the choices are made for the substitution of tendencies
    # result is a list of tuples with the structure (a,b,c) where
    #                                                   a = pagenumber
    #                                                   b = squarenumber
    #                                                   c = tendency number
    all_tuples = []
    for p in range(0,7): # all pages, used as index for instructions
        instr = instructions[p]
        pagenr = p+1
        for n in range(0, 3): # there are three possible instruction sets per page
            if bool(instr[n]):  # meaning: if not empty
                times = instr[n]['times']
                squares_involved = instr[n]['squares']
                to_be_replaced_by = instr[n]['replaced by']
                # times is optional, so there may be less than times
                times = random.choice(range(0,times+1))
                chosen_squares = random.sample(squares_involved,times) # sample method, to avoid repeating the same choices
                #for m in range(1, times + 1):
                    # choose which squares TODO nog bepalen of de keuze wel wordt gemaakt (want kan ook worden overgeslagen)
                #    chosen_square = random.choice(squares_involved) #TODO nog wel toetsen of het nummer al niet eerder is gekozen
                #    chosen_squares.append(chosen_square)
                for sq in chosen_squares:
                    if type(sq) == list: # which is only the case in page 2, where two numbers are collected here
                        result_tuple = (pagenr, sq[0], to_be_replaced_by[0])
                        all_tuples.append(result_tuple)
                        result_tuple = (pagenr, sq[1], to_be_replaced_by[1])
                        all_tuples.append(result_tuple)
                    else:
                        result_tuple = (pagenr, sq, to_be_replaced_by[0])
                        all_tuples.append(result_tuple)
    return all_tuples


config2e = make_choices_for_tendency_substitutes() # not fixed, but changing everytime

def get_config2():
    return config2a