# functions to gather input from user and write it to a config file in json format

import json
from numpy.random import seed
from numpy.random import shuffle

def answer_method_dialog():
    question = "method of answering: random (r), input (i) or default (d)"
    answer = ""
    while answer not in ['r','i','d']:
        answer = input(question)
    return answer

def get_number_of_layers():
    # gather input from user
    n_layers = int(input("Number of layers: "))
    return n_layers

def get_page_orders(n):

    print("ORDER OF SQUARE PAGES")
    order_of_squarepages = []
    method = answer_method_dialog()
    if method == "i" :
        for n in range(1, 8):
            print(order_of_squarepages)
            question = "position " + str(n) + ": "
            input_n = int(input(question))
            while (input_n in order_of_squarepages) or (input_n > 7) or (input_n < 1):
                print("sorry, again")
                input_n = int(input(question))
            order_of_squarepages.append(input_n)
    elif method == 'd':
        # default values
        order_of_squarepages = [1,2,3,4,5,6,7]
    elif method == 'r':
        # random generator
        order_of_squarepages = [1, 2, 3, 4, 5, 6, 7]
        shuffle(order_of_squarepages)

    print("ORDER OF NOTE PAGES")
    order_of_notepages = []
    method = answer_method_dialog()
    if method == 'i':
        for n in range(1, 8):
            print(order_of_notepages)
            question = "position " + str(n) + ": "
            input_n = int(input(question))
            while (input_n in order_of_notepages) or (input_n > 7) or (input_n < 1):
                print("sorry, again")
                input_n = int(input(question))
            order_of_notepages.append(input_n)
    elif method == 'd':
        order_of_notepages = [1,2,3,4,5,6,7]
    elif method == 'r':
        # random generator
        order_of_notepages = [1, 2, 3, 4, 5, 6, 7]
        shuffle(order_of_notepages)

    return n, order_of_squarepages, order_of_notepages


def write_to_config(list_of_layers):
    # Data to be written
    my_dict = {}
    my_list_of_dict = []
    for d in list_of_layers:
        layer_dict = {
            "layer": d[0],
            "order of square pages": d[1],
            "order of note pages": d[2]
        }
        my_list_of_dict.append(layer_dict)

    

        #dictionary.append(tussen_dict)  ##this does not work!

    with open("setup_config.json", "w") as outfile:
        json.dump(my_dict, outfile)


# Opening JSON file
def read_config():
    with open('setup_config.json', 'r') as openfile:
    # Reading from json file
        json_object = json.load(openfile)
    print(json_object)
    #print(type(json_object))

# test
layers = get_number_of_layers()
all_layers_page_orders = []
for n in range(1,layers+1):
    orders = get_page_orders(n)
    #print(orders)
    all_layers_page_orders.append(orders)

#clear the json file
open('setup_config.json','w').close()

resulting_list = []
for layer in all_layers_page_orders:
    #print(layer)
    print(layer[0], layer[1], layer[2])
    resulting_list.append(layer)

#write_to_config(resulting_list)
print(resulting_list)
print(type(resulting_list))
#read_config()