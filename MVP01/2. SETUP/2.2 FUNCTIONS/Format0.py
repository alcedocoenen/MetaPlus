#Format0.py

# functions for composing the squarepages according to a chosen number of layers and order of pagesd.
# Main functions:
# 1. DefineNumberOfLayers: Number of layers has to be defined.
# 2. MapPages: For each layer, the mapping and order of pages has to be defined
# 3. ChangeSubstitutions: The increase and decrease signs have to be replaced according to the page instructions.

# bracketfilling is OUT OF SCOPE here because it can only be handled after the squares are completely transformed into musical events.
# BracketFilling: The brackets have to be filled with the right number of squares

import Configurations as cf
import ReadWriteSquares as rws
import random
import PlusMinusIndexes as pm_index
import time

#use the config1 variable for this step.



# for each layer:
#       1. replace the tendency values 4 with increase or decrease
#       2. substitute tendencies according to bottom page instructions
# then write complete new object with layer number


def convert_stage0_to_stage0a(stage0_squares, version, choice = cf.config0a_a):
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
    rws.write_object(tendency,version)
    for square in stage0_squares:
        count +=1
        if count != 1: # skip the header row
            index_number_in = pm_index.square_format0_index_dict["increase"]
            index_number_de = pm_index.square_format0_index_dict["decrease"]
            if square[index_number_in] == "4": # if this is 4, both are 4 in format 0
                logtext = "current square = " + str(square)
                rws.write_log(logtext, version)

                if choice == "random per case":
                    tendency = random.choice(list_of_possibilities)
                if tendency == "increase":
                    square[index_number_in] = "4"
                    square[index_number_de] = "0"
                elif tendency == "decrease":
                    square[index_number_in] = "0"
                    square[index_number_de] = "4"
                logtext = "new square = " + str(square)
                rws.write_log(logtext, version)
            stage0a_squares.append(square)
    return stage0a_squares


def convert_stage0a_to_stage0b(stage0a_squares, choice_tuple_list, version):
    stage0b_squares = []
    #print(choice_tuple_list)
    for square in stage0a_squares:
        index_pagenumber = pm_index.square_format0_index_dict["pagenumber"]
        index_number_in = pm_index.square_format0_index_dict["increase"]
        index_number_de = pm_index.square_format0_index_dict["decrease"]
        index_square_number = pm_index.square_format0_index_dict["real_number"]
        # for each page separate instructions
        pagenr = int(square[index_pagenumber])
        squarenr = int(square[index_square_number])
        increase = int(square[index_number_in])
        decrease = int(square[index_number_de])

        for t in choice_tuple_list:
            if t[0] == pagenr:
                if t[1] == squarenr:
                    rws.write_log(square,version)
                    if increase != 0:
                        square[index_number_in] = str(t[2])
                    elif decrease != 0:
                        square[index_number_de] = str(t[2])
                    rws.write_log("is now replaced by",version)
                    rws.write_log(square,version)
        stage0b_squares.append(square)

    return stage0b_squares



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

#number_of_layers = len(layer_config.keys())

def convert_stage0b_to_stage0c(stage0b_squares, orderlist):
    # stage0c is having the pages in the chosen order
    stage0c_squares = []

    # TODO first get each page from stage0b in a separate list variable.
    page1 = []
    page2 = []
    page3 = []
    page4 = []
    page5 = []
    page6 = []
    page7 = []
    list_of_pages = [page1, page2, page3, page4, page5, page6, page7]

    #read the squares from stage0b, and attribute each square to the page-list according to the orderlist.

    index_pagenumber = pm_index.square_format0_index_dict["pagenumber"]

    for square in stage0b_squares:
        pagenr = int(square[index_pagenumber])

        if pagenr == orderlist[0]:
            page1.append(square)
        elif pagenr == orderlist[1]:
            page2.append(square)
        elif pagenr == orderlist[2]:
            page3.append(square)

        elif pagenr == orderlist[3]:
            page4.append(square)

        elif pagenr == orderlist[4]:
            page5.append(square)

        elif pagenr == orderlist[5]:
            page6.append(square)

        elif pagenr == orderlist[6]:
            page7.append(square)


    # the list_of_pages is now in the right order.
    # the list_of_pages has to be brought back to one long list

    for page in list_of_pages:
        for square in page:
            stage0c_squares.append(square)

    return stage0c_squares




def define_filename(filename, ext, version, layer):
    if not(version):
        version = time.strftime("%Y%m%d-%H%M%S")
    file_result = rws.datapath + filename + '_V' + version + '_L' + layer + '.' + ext
    return file_result


# ====== making the conversions in files =======

def make_format_0a(rawlist, version, layer):
    # this functions converts the format 0 file into a format 0a file with restitution of the 4-tendency values
    # this needs to be done for each layer separately
    #allsquares = rws.get_all_squares_as_rawlist()
    rws.write_log("writing format 0a", version)
    fname = rawlist
    file_to_open = rws.datapath+fname
    allsquares = rws.open_plusminus_squares_rawlist(file_to_open,",")
    config = cf.getconfig0()
    result = convert_stage0_to_stage0a(allsquares, version, config)
    fname = rws.filenamebase + '_Format0a'
    file_to = define_filename(fname,'csv', version, layer)
    rws.write_raw_list(file_to, result)

    rws.write_log(config, version)
    rws.write_log(file_to, version)
    rws.write_log("end of conversion stage0 => stage0a", version)
    return "format 0a written"

def make_format_0b(version, layer):
    # this function coverts the format 0a file into a format 0b file with replacement of all tendency values according to page instructions
    rws.write_log("writing format 0b", version)
    fname = rws.filenamebase + '_Format0a'
    file_to_open = define_filename(fname,'csv', version, layer)
    allsquares = rws.open_plusminus_squares_rawlist(file_to_open,",")
    config =  cf.get_config2() # refer to configurations file for a valid tuple list
    result = convert_stage0a_to_stage0b(allsquares, config, version)
    fname = rws.filenamebase + '_Format0b'
    file_to_write = define_filename(fname,'csv', version, layer)
    rws.write_raw_list(file_to_write, result)

    rws.write_log(config, version)
    rws.write_log(file_to_write, version)
    rws.write_log("end of conversion stage0a => stage0b", version)
    return " format 0b written"

def make_format_0c(version, layer):
    rws.write_log("writing format 0c", version)
    fname = rws.filenamebase + '_Format0b'
    file_to_open = define_filename(fname,'csv', version, layer)
    allsquares = rws.open_plusminus_squares_rawlist(file_to_open,",")
    #config =  cf.get_config1()
    orderlist = cf.get_order_of_squarepages(int(layer))
    result = convert_stage0b_to_stage0c(allsquares, orderlist)
    fname = rws.filenamebase + '_Format0c'
    file_to_write = define_filename(fname,'csv', version, layer)
    rws.write_raw_list(file_to_write, result)

    rws.write_log(orderlist, version)
    rws.write_log(file_to_write, version)
    rws.write_log("end of conversion stage0b => stage0c", version)

    return "format 0c written"



# ========= EXECUTION ===========
# some global variables, to be defined in a config

def make_them_all(version):
    #for each layer
    # get nr of layers first
    nr_of_layers = cf.get_number_of_layers()
    for i in range(nr_of_layers):
        layer = str(i+1)
        make_format_0a('PlusMinusDataSquaresAsRawList',version, layer)
        make_format_0b(version,layer)
        make_format_0c(version, layer)

make_them_all('001')
# === divers tests
