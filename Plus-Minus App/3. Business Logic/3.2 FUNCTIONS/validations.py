
def validated(pages):
    # function to assure the entered numbers for the pages are correct.
    # if not correct, it should be corrected automatically
    # the return is a valid list of exluding numbers 1-7

    #first check if pages is a list or not
    # sample list
    is_not_empty_list = False
    is_string_of_numbers = False
    is_wrong = False

    if isinstance(pages,list):
        # check if the list is empty
        if len(pages) == 0:
            is_wrong = True
        else: is_not_empty_list = True
    elif isinstance(pages,str):
        #filter out characters in the list
        #pages = list(filter(lambda x: isinstance(x,int), pages))
        temp_p = ""
        for x in pages:
            if x.isnumeric():
                temp_p = temp_p + x
        pages = temp_p

        # check if the list is empty
        if len(pages) == 0:
            is_wrong = True
        elif pages.isnumeric(): #exclude a string of characters which are not numbers
            is_string_of_numbers = True
    else:
        is_wrong = True

    #if not a list but a string, then make a list
    if is_string_of_numbers:
        pages_list = []
        for i in pages:
            j = int(i)
            pages_list.append(j)
        pages = pages_list
        is_not_empty_list = True

    if is_not_empty_list:




        #check the validity of numbers
        # if > 7 then replace by 7
        temp_list = list(map(lambda x: 7 if x > 7 else x, pages))
        # if = 0 the replace by 1
        new_list = list(map(lambda x: 1 if x < 1 else x, temp_list))
        pages = new_list

        # check exclusivity
        newList = []
        for item in pages:
            if item not in newList:
                newList.append(item)
        pages = newList

        #because of the uniqueness and value < 8, this list an only be 7 or shorter
        # if too short, it needs to be extended with the missing numbers
        if len(pages) < 7:
            validrange = range(7)
            for x in validrange:
                if x+1 not in pages:
                    pages.append(x+1)

        # return a string
        result = ""
        for x in pages:
            result = result + str(x)

        pages = result

    if is_wrong:
        pages = "1234567"



    return pages


# some tests
'''
test1 = "a5b8c3"
test2 = [7,6,5,4,3]
test3 = "9760162345"
test4 = "351"
test5 = 15.690
test6 = "4521367"
test7 = "abc"
test8 = "6565432"

print(validated(test1))
print(validated(test2))
print(validated(test3))
print(validated(test4))
print(validated(test5))
print(validated(test6))
print(validated(test7))
print(validated(test8))
'''


