# config.py
# this file is meant to collect all setup and config parameters
# instead of using a GUI for asking.
# later this can be replaced by a genuine GUI that reads and writes confi files.

# ============== CONFIG 0a ====================
# config 0a is about replacing the 4-tendencies with one of them
# re: rule 20 in the instructions.

config0a_a = "random once defined"
config0a_b = "random per case"
config0a_c = "increase"
config0a_d = "decrease"



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
                      "order of squarepages": [3, 5, 2, 4, 1, 6, 7],
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

# here is the main variable. Change this when choosing another configuration
def get_config1():
    return config1a


#=============== CONFIG 2 =====================
# Config2 is about square substitution
