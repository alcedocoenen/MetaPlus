
def validated(pages):
    # function to assure the entered numbers for the pages are correct.
    # if not correct, it should be corrected automatically
    # the return is a valid list of exluding numbers 1-7

    #first check if pages is a list or not
    # sample list
    is_list = False
    is_string = False
    is_wrong = False

    if isinstance(pages,list):
        is_list = True
    elif isinstance(pages,str):
        is_string = True
    else:
        is_wrong = True

    #if not a list but a string, then make a list
    pages_list = []
    if is_string:
        for i in pages:
            j = int(i)
            pages_list.append(j)
        pages = pages_list
        is_list = True
        is_string = False

    if is_list:
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

    if is_wrong:
        pages = []

    #return a string
    result = ""
    for x in pages:
        result = result + str(x)

    pages = result

    return pages


# some tests
'''
test1 = "6565432"
test2 = [7,6,5,4,3]
test3 = "9760162345"
test4 = "351"
test5 = 1.23
test6 = "4521367"

print(validated(test1))
print(validated(test2))
print(validated(test3))
print(validated(test4))
print(validated(test5))
print(validated(test6))

'''

