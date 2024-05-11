# ReadWriteSquares
# routines for reading the Squarepages in csv format, and convert it to a Dict/List object
# only to be used once, because the Squarepages are fixed, and the object should be a fixed object.

from csv import DictReader
import csv
import pickle
import PlusMinusIndexes as pm_index

datapath = '/Users/alcedocoenen/Documents/Plus-Minus/Python/MetaPlus/MetaPlus/MVP01/1. LOAD/1.1 DATA/'

def open_plusminus_squares(filename):
    # valid for all formats between 0 and ...
    with open(filename, mode='r') as file:
        dictfile = DictReader(file, delimiter=";")
        list_of_dict = list(dictfile)
    return list_of_dict

def open_plusminus_squares_rawlist(filename, delim = ";"):
    # delim = ";" is valid for original PlusMinusDataSquares.csv
    # delim = "," is valid for PlusMinusDataSquaresAsRawList
    # valid for all formats between 0 and ...
    rawlist = []
    with open(filename) as pm_file:
        pm_reader = csv.reader(pm_file, delimiter = delim)
        for row in pm_reader:
            rawlist.append(row)
    return rawlist

def write_raw_list(filename, rawlist):
    # valid for all formats between 0 and ...
    with open(filename, 'w', newline='') as csvfile:
        pm_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for r in rawlist:
            pm_writer.writerow(r)
    return "wrote rawlist to file"


# FORMAT 0: [1,11,10,0,0,6,3,0,1,0,0,0,0,0,0,0,0,0,0,2,3,4,4,0,1]
# need to be converted to dictionary structure
#   'nrs': {'sqnr_seq': '1', 'sqnr': '1'},
#   'boldness': '1',
#   'Brackets': '0',
#   'Centralsound': {'centralsound': '4', 'type': '7'},
#   'Dur_rest': {'durartion': '0', 'rest': '1'},
#   'Accidents': {'pre-bot': '2', 'pre-top': '0', 'mid-bot': '3', 'mid-top': '2', 'post_bot': '3', 'post_top': '0'},
#   'Nebennoten': {'position': '0', 'number': '0', 'speed': '0'},
#   'Flag': {'top': '-3', 'bottom': '0'},
#   'Coordination': {'timing': '0', 'pitch': '1'},
#   'Tendencies': {'increase': '1', 'decrease': '0'},
#   'Effect': '1'}
#
# nrs:
# 	pagenumber: SymbolPage.Number
# 	sequence_nr: Square.SequenceNumber,
# 	real_number: Square.Number
# square_characteristics:
# 	boldness: Boldness,
# 	brackets: Brackets
# music events:
# 	centralsound: Centralsound
# 	type: Type
# 	duration: Duration
# 	rest: Rest
# 	accidents:
# 		pre-bot: A-pre-bot
# 		pre-top: A-pre-top
# 		mid-bot: A-cen-bot
# 		mid-top: A-cen-top
# 		post-bot: A-pos-bot
# 		post-top: A-pos-top
# 	nebennoten:
# 		position: Nebennoten.Position
# 		number: Nebennoten.Number
# 		speed: Nebennoten.Speed
# flag:
# 	top: Flag.Top
# 	bottom: Flag.Bottom
# coordination:
# 	timing: Coordination.Timing
# 	pitch: Coordination.Pitch
# tendencies:
# 	increase: Tendency.Increase
# 	decrease: Tendency.Decrease
# effect: Effect
'''
square_format0_index_dict = {
    "pagenumber": 0,
    "sequencenr": 1,
    "real_number": 2,
    "boldness": 3,
    "brackets": 4,
    "centralsound": 5,
    "duration": 6,
    "rest": 7,
    "pre-bot": 8,
    "pre-top": 9,
    "mid-bot": 10,
    "mid-top": 11,
    "post-bot": 12,
    "post-top":13,
    "neben_position": 14,
    "neben-number": 15,
    "neben-speed": 16,
    "flag-top": 17,
    "flag-bottom": 18,
    "coord-timing": 19,
    "coord-pitch": 20,
    "increase": 21,
    "decrease": 22,
    "effect": 23,
    "type": 24
}
'''

def read_raw_square(square):
    formatted_square_string=""
    nrs = "nrs: \n\tpagenumber: " + square[0] + "\n\tsequence_nr: " + square[1] + ", \n\treal_number: " + square[2]
    square_characteristics = "\nsquare_characteristics: \n\tboldness: " + square[3] + ", \n\tbrackets: " + square[4]
    music_events = "\nmusic events: \n\tcentralsound: " + square[5] + "\n\ttype: " + square[24] + "\n\tduration: " + square[6] + \
                   "\n\trest: " + square[7] + "\n\taccidents: " \
                                            + "\n\t\tpre-bot: " + square[8] + "\n\t\tpre-top: " + square[9] \
                                            + "\n\t\tmid-bot: " + square[10] + "\n\t\tmid-top: " + square[11] \
                                            + "\n\t\tpost-bot: " + square[12] + "\n\t\tpost-top: " + square[13] \
                    + "\n\tnebennoten: " + "\n\t\tposition: " + square[14] \
                                         + "\n\t\tnumber: " + square[15] \
                                         + "\n\t\tspeed: " + square[16]
    flag = "\nflag: " + "\n\ttop: " + square[17] + "\n\tbottom: " + square[18]
    coordination = "\ncoordination: " + "\n\ttiming: " + square[19] + "\n\tpitch: " + square[20]
    tendencies = "\ntendencies: " + "\n\tincrease: " + square[21] + "\n\tdecrease: " + square[22]
    effect = "\neffect: " + square[23]
    formatted_square_string = nrs + square_characteristics + music_events + flag + coordination + tendencies + effect
    return formatted_square_string

# filename = "PlusMinusResultTest.csv"
def writeplusminus_csv(filename, content):
    pagefilename = filename
    with open(pagefilename, mode='w') as targetfile:
        for lines in content:
            for squares in lines:
                targetfile.write(squares[0])
                targetfile.write('\n')


def write_object(filename, content):
    with open(filename, 'wb') as binaryfile:
        pickle.dump(content, binaryfile)
        print("written to binary file")


def read_object(filename):
    with open(filename, 'rb') as objectfile:
        complete_list = pickle.load(objectfile)
        return complete_list


def print_list_of_dict(list_of_dict):
    for square in list_of_dict:
        print(square)

# csv square format is: PageNumber;
#                       SequenceNumber;
#                       SquareNumber;
#                       Boldness;
#                       Brackets;
#                       Centralsound;
#                       Duration;
#                       Rest;
#                       A-pre-bot;
#                       A-pre-top;
#                       A-cen-bot;
#                       A-cen-top;
#                       A-pos-bot;
#                       A-pos-top;
#                       NebennotenPosition;
#                       NebennotenNumber;
#                       NebennotenSpeed;
#                       Flag.Top;
#                       Flag.Bottom;
#                       Coordination.Timing;
#                       Coordination.Pitch;
#                       Tendency.Increase;
#                       Tendency.Decrease;
#                       Effect;
#                       Type
# 1;11;10;0;0;6;3;0;1;0;0;0;0;0;0;0;0;0;0;2;3;4;4;0;1
# need to be converted to dictionary structure
# {'nrs': {'sqnr_seq': '1', 'sqnr': '1'},
#   'boldness': '1',
#   'Brackets': '0',
#   'Centralsound': {'centralsound': '4', 'type': '7'},
#   'Dur_rest': {'durartion': '0', 'rest': '1'},
#   'Accidents': {'pre-bot': '2', 'pre-top': '0', 'mid-bot': '3', 'mid-top': '2', 'post_bot': '3', 'post_top': '0'},
#   'Nebennoten': {'position': '0', 'number': '0', 'speed': '0'},
#   'Flag': {'top': '-3', 'bottom': '0'},
#   'Coordination': {'timing': '0', 'pitch': '1'},
#   'Tendencies': {'increase': '1', 'decrease': '0'},
#   'Effect': '1'}
#
# total object format  =
#   (


def convert_to_structured_dict_format0(content):
    # content is supposed to be a list of dictionaries, each dictionary representing a square

    list_of_square_dict = []
    list_of_symbolpages = []

    current_pagenr_i = 0
    page_dict = {}

    for square in content:
        square_dict = {}
        nr_dict = {}
        acc_dict = {}
        sound_dict = {}
        durrest_dict = {}
        nebennoten_dict = {}
        flag_dict = {}
        coord_dict = {}
        tendency_dict = {}

        pagenr = square["\ufeffSymbolPage.Number"]
        pagenr_i = int(pagenr)
        if pagenr_i != current_pagenr_i and current_pagenr_i != 0:  # dat wil zeggen dat er een nieuwe pagina is gearriveerd
            # in dat geval moet er een nieuwe page-dict worden aangemaakt, gevuld met de list_of_square_dict
            page_dict["nr"] = str(pagenr_i-1)  # de voorlaatste page wordt nu eerst opgeslagen
            page_dict["squares"] = list_of_square_dict  # dat is dus de lijst van squares die tot nu toe is opgebouwd
            list_of_symbolpages.append(page_dict)  # toevoegen aan het eindresultaat van dexe functie
            page_dict = {}  # leeg
            list_of_square_dict = []  # nu weer leeg
            current_pagenr_i = pagenr_i
        else:
            current_pagenr_i = pagenr_i
        # in alle andere gevallen dus niets doen met de pagenr, maar alle squares verzamelen

        sqnr_seq = square["Square.SequenceNumber"]
        sqnr = square["Square.Number"]
        nr_dict["sqnr_seq"] = sqnr_seq
        nr_dict["sqnr"] = sqnr
        square_dict["Numbers"] = nr_dict

        bold = square["Boldness"]
        square_dict["Boldness"] = bold

        brackets = square["Brackets"]
        square_dict["Brackets"] = brackets

        centralsound = square["Centralsound"]
        soundtype = square["Type"]
        sound_dict["centralsound"] = centralsound
        sound_dict["type"] = soundtype
        square_dict["Centralsound"] = sound_dict

        duration = square["Duration"]
        rest = square["Rest"]
        durrest_dict["durartion"] = duration
        durrest_dict["rest"] = rest
        square_dict["Dur_rest"] = durrest_dict

        acc1 = square["A-pre-bot"]
        acc2 = square["A-pre-top"]
        acc3 = square["A-cen-bot"]
        acc4 = square["A-cen-top"]
        acc5 = square["A-pos-bot"]
        acc6 = square["A-pos-top"]
        acc_dict["pre-bot"] = acc1
        acc_dict["pre-top"] = acc2
        acc_dict["mid-bot"] = acc3
        acc_dict["mid-top"] = acc4
        acc_dict["post_bot"] = acc5
        acc_dict["post_top"] = acc6
        square_dict["Accidents"] = acc_dict

        n_pos = square["Nebennoten.Position"]
        n_num = square["Nebennoten.Number"]
        n_speed = square["Nebennoten.Speed"]
        nebennoten_dict["position"] = n_pos
        nebennoten_dict["number"] = n_num
        nebennoten_dict["speed"] = n_speed
        square_dict["Nebennoten"] = nebennoten_dict

        flag_top = square["Flag.Top"]
        flag_bot = square["Flag.Bottom"]
        flag_dict["top"] = flag_top
        flag_dict["bottom"] = flag_bot
        square_dict["Flag"] = flag_dict

        coord_time = square["Coordination.Timing"]
        coord_pitch = square["Coordination.Pitch"]
        coord_dict["timing"] = coord_time
        coord_dict["pitch"] = coord_pitch
        square_dict["Coordination"] = coord_dict

        tendency_incr = square["Tendency.Increase"]
        tendency_decr = square["Tendency.Decrease"]
        tendency_dict["increase"] = tendency_incr
        tendency_dict["decrease"] = tendency_decr
        square_dict["Tendencies"] = tendency_dict

        effect = square["Effect"]
        square_dict["Effect"] = effect

        list_of_square_dict.append(square_dict)

    # de laatste page (7) moet nog worden opgeslagen
    page_dict["nr"] = "7"  # de laatste page wordt nu opgeslagen
    page_dict["squares"] = list_of_square_dict  # dat is dus de lijst van squares die tot nu toe is opgebouwd
    list_of_symbolpages.append(page_dict)  # toevoegen aan het eindresultaat van dexe functie

    return list_of_symbolpages


# main routine
def execute_conversion(csvfile, objectfile):
    # for format 0 only
    dict_squares = open_plusminus_squares(csvfile)
    structured_list = convert_to_structured_dict_format0(dict_squares)
    write_object(objectfile, structured_list)
    print_list_of_dict(structured_list)
    return len(structured_list)


def check_result(objectfile):
    # valid for any objectfile that has a list
    result = read_object(objectfile)
    print_list_of_dict(result)
    return len(result)


def readPlusMinusObject(objectfilename):
    return read_object(objectfilename)


def get_all_squares_as_rawlist(csvfile = datapath + 'PlusMinusDataSquares.csv'):
    # format 0 only
    rawlist = open_plusminus_squares_rawlist(csvfile)
    return rawlist


def get_all_squares_as_dict(csvfile = datapath + 'PlusMinusDataSquares.csv'):
    # format 0 only
    dict_squares = open_plusminus_squares(csvfile)
    structured_list = convert_to_structured_dict_format0(dict_squares)
    return structured_list



def find_square_numbers_in_page_in_rawlist(page, field, value, format = 0):
    # first check if field name is valid
    if isinstance(value, int):
        value = str(value)
    if format == 0:
        if field in pm_index.square_format0_index_dict.keys():
            list_of_square_numbers = []
            all_squares = get_all_squares_as_rawlist()
            square_count = 1
            for square in all_squares:
                if square_count > 1:
                    if int(square[0]) == page:
                        if square[pm_index.square_format0_index_dict[field]] == value:
                            sqnr = square[pm_index.square_format0_index_dict["real_number"]]
                            if isinstance(sqnr, str):
                                sqnr = int(sqnr)
                            list_of_square_numbers.append(sqnr)
                square_count +=1
            return list_of_square_numbers
        else:
            return "invalid field name"
    else:
        return "format non existing"


def write_log(content, version):
    logfile = datapath + "PlusMinus_Log_V_" + version + ".log"
    if type(content) != str:
        content = str(content)
    with open(logfile, mode='a') as targetfile:
            targetfile.write(content)
            targetfile.write('\n')

# =================== TESTING ======================

# really execute now
#print(execute_conversion('PlusMinusDataSquares.csv', 'PlusMinusDataSquaresObject'))
#print(check_result('PlusMinusDataSquaresObject'))

# optionally read the objectfile only
#print(readPlusMinusObject('PlusMinusDataSquaresObject'))

result = open_plusminus_squares_rawlist(datapath+'PlusMinusDataSquares.csv')
print(write_raw_list(datapath+'PlusMinusDataSquaresAsRawList', result))
print(read_raw_square(result[0])) # toprow = header
print(read_raw_square(result[len(result)-1])) # last row

# search for sample values
#print(find_square_numbers_in_page_in_rawlist(6, "increase", 3))
#print(find_square_numbers_in_page_in_rawlist(7, "increase", 1))
#print(find_square_numbers_in_page_in_rawlist(5, "increase", 1))
#print(find_square_numbers_in_page_in_rawlist(5, "decrease", 3))
