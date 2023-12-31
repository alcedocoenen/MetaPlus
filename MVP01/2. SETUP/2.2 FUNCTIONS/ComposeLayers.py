#ComposeLayers.py

# functions for composing the squarepages according to a chosen number of layers and order of pagesd.
# Main functions:
# 1. DefineNumberOfLayers: Number of layers has to be defined.
# 2. MapPages: For each layer, the mapping and order of pages has to be defined
# 3. BracketFilling: The brackets have to be filled with the right number of squares
# 4. ChangeSubstitutions: The increase and decrease signs have to be replaced according to the page instructions.

import Configurations as cf
import ReadWriteSquares as rws
import random
import PlusMinusIndexes as pm_index

#use the config1 variable for this step.


# config structure:
# {
#                 1:
#                      {"layernr" : 1,
#                       "order of squarepages": [3, 5, 2, 4, 1, 6, 7],
#                       "order of notepages": [4, 5, 6, 7, 3, 2, 1]
#                       },
#                 2:
#                      {"layernr" : 2,
#                       "order of squarepages": [3, 5, 2, 4, 1, 6, 7],
#                       "order of notepages": [4, 5, 6, 7, 3, 2, 1]
#                       }
# }

layer_config = cf.get_config1()
number_of_layers = len(layer_config.keys())

# for each layer:
#       1. replace the tendency values 4 with increase or decrease
#       2. substitute squares according to arrow instructions
#       2. substitute tendencies according to bottom page instructions
# then write complete new object with layer number


def convert_stage0_to_stage0a(stage0_squares, choice = cf.config0a_a):
    # squares as list
    # stage 0a is with 4-tendencies replaces
    # this is called 0a because it does not change the format
    stage0a_squares = []
    tendency = ''
    list_of_possibilities = ["increase", "decrease"]
    count = 0
    if choice == "random once defined":
        tendency = random.choice(list_of_possibilities)
    elif choice != "random per choice":
        tendency = choice
    for square in stage0_squares:
        count +=1
        if count != 1: # skip the header row
            index_number_in = pm_index.square_format0_index_dict["increase"]
            index_number_de = pm_index.square_format0_index_dict["decrease"]
            if square[index_number_in] == "4": # if this is 4, both are 4 in format 0
                if choice == "random per choice":
                    tendency = random.choice(list_of_possibilities)
                if tendency == "increase":
                    square[index_number_in] = "4"
                    square[index_number_de] = "0"
                elif tendency == "decrease":
                    square[index_number_in] = "0"
                    square[index_number_de] = "4"
            stage0a_squares.append(square)
    return stage0a_squares

def replace_brackets(square):
    # need to read the arrows score data
    return square

def tendency_substitutions(page):
    # need to read the tendency instructions data
    return page


def convert_stage0_to_stage1(stage0_squares):
    # stage0 is the original score, stage1 is the first transformation
    stage1_squares = []
    return stage1_squares


# ====== execution =======

def make_format_0a():
    # this needs to be done for each layer separately
    allsquares = rws.get_all_squares_as_rawlist()
    result = convert_stage0_to_stage0a(allsquares)
    file_to = rws.datapath + 'PlusMinusDataSquaresFormat0a.csv'
    rws.write_raw_list(file_to,result)
    return "format 0a written"

make_format_0a()