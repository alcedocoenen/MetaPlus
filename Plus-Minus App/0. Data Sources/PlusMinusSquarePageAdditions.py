# data structures for additional instructions on the square pages
# the data structures are made in plain python dictionary format

# =========== SQUARE SUBSTITUTIONS ==================
# pas = page arrow statements
# this refers to the arrows on top of each symbol page, meant to substitute squares that are in "brackets"

pas1 = [
    {"top":
            {"arrow_at_left_side": "left",
            "arrow_at_left_comment": "entweder",
            "arrow_at_right_side": "right",
            "arrow_at_right_Comment": "oder"}},
    {"bottom":
            {}
     },
    {"bold_squares": [1, 4, 42]}
]

pas2 = [
    {"top":
            {"arrow_at_left_side": "",
            "arrow_at_left_comment": "",
            "arrow_at_right_side": "",
            "arrow_at_right_Comment": ""}
     },
    {"bottom":
            {}
     },
    {"bold_squares": [1, 43]}
]

pas3 = [
    {"top":
           {"arrow_at_left_side": "right",
            "arrow_at_left_comment": "",
            "arrow_at_right_side": "left",
            "arrow_at_right_Comment": "2"}
     },
    {"bottom":
           {"arrow_at_left_side": "left",
            "arrow_at_left_comment": "entweder",
            "arrow_at_right_side": "right",
            "arrow_at_right_Comment": "oder"}
     },
    {"bold_squares": [2, 7, 51]}
]

pas4 = [
    {"top":
            {"arrow_at_left_side": "right",
            "arrow_at_left_comment": "2",
            "arrow_at_right_side": "left",
            "arrow_at_right_Comment": "3"}
     },
    {"bottom":
            {"arrow_at_left_side": "left",
            "arrow_at_left_comment": "",
            "arrow_at_right_side": "right",
            "arrow_at_right_Comment": ""}
     },
    {"bold_squares": [1, 2, 52, 53]}
]

pas5 = [
    {"top":
            {"arrow_at_left_side": "right",
            "arrow_at_left_comment": "",
            "arrow_at_right_side": "left",
            "arrow_at_right_Comment": ""}
     },
    {"bottom":
            {}
     },
    {"bold_squares": [7, 53]}
]

pas6 = [
    {"top":
            {"arrow_at_left_side": "",
            "arrow_at_left_comment": "",
            "arrow_at_right_side": "left",
            "arrow_at_right_Comment": ""}
     },
    {"bottom":
            {}
     },
    {"bold_squares": [2, 53]}
]

pas7 = [
    {"top":
            {"arrow_at_left_side": "left",
            "arrow_at_left_comment": "",
            "arrow_at_right_side": "right",
            "arrow_at_right_Comment": ""}
     },
    {"bottom":
            {}
     },
    {"bold_squares": [1, 2, 51, 53]}
]

page_arrow_statements = [pas1, pas2, pas3, pas4, pas5, pas6, pas7]


# ================= TENDENCY SUBSTITUTIONS =====================
# pts = page tendency statements
# this refers to the instructions at the bottom of the symbol pages, for replacing tendencies within specific squares.
pts1 = [{},{},{}]
pts2 = \
    [{"times": 1,
        "squares": [[5,6],[27,28],[47,49]],
        "replaced by": [7,14]},
     {},{}]
pts3 = \
    [{"times": 5,
        "squares": [8,9,13,39,41],
        "replaced by": [7]},
     {},{}]
pts4 = \
    [{"times": 2,
        "squares": [1,3,5,7,9,11,13,15,17,19,21,35,37,39,41,43,45,47,49,51,53], # all squares with (increase, 2)
        "replaced by": [14]},
     {},{}]
pts5 = \
    [{"times": 2,
         # find_square_numbers_in_page_in_rawlist(5, "decrease", 3)
        "squares": [2,4,7,9,12,14,17,19,22,24,26,29,31,33,36,38,41,46,49,53], # all squares with (decrease, 3)
        "replaced by": [7]},
     {"times": 1,
      # find_square_numbers_in_page_in_rawlist(5, "increase", 1)
      "squares": [1, 3, 6, 10, 15, 21, 28, 34, 39, 44, 48, 51, 52],
      # all squares with tendency (increase, 1) value
      "replaced by": [7]},
     {}]
pts6 = \
    [{"times": 1,
         # [1, 7, 9, 14, 16, 20, 22, 25, 27, 30, 32, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53]
         # find_square_numbers_in_page_in_rawlist(6, "increase", 3)
        "squares": [1,7,9,14,16,20,22,25,27,30,32,35,37,39,41,43,45,47,49,51,53], # all squares with (increase, 3)
        "replaced by": [9]},
     {"times": 1,
      "squares": [2, 11, 19, 23, 29, 33, 38, 40, 44, 46, 50, 52],
      # all squares with (decrease, 4) ONLY VALID WHEN 4/4 HAS BEEN CHOSEN
      "replaced by": [12]},
     {"times": 1,
        "squares": [2,11,19,23,29,33,38,40,44,46,50,52], # all squares with (increase, 4) ONLY VALID WHEN 4/4 HAS BEEN CHOSEN
        "replaced by": [12]}]
pts7 = \
    [{"times": 1,
         # find_square_numbers_in_page_in_rawlist(7, "increase", 1)
         # [31, 34, 36, 38, 41, 43, 46, 49]
        "squares": [31,34,36,38,41,43,46,49], # all squares with (increase, 1)
        "replaced by": [7,14]},
     {},{}]

page_tendency_statements = [pts1, pts2, pts3, pts4, pts5, pts6, pts7]

