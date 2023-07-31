# this function takes as argument a string and a path to a dictionary
# the string gets split into all possible two letter combinations
# then the dictionary is searched for these two letter combinations
# a table of occurence counts is returned
# QBA LIU 2023 ---------------------------------------------------------------------------------------------------------------


def occurence_count(string, path_to_dict):
    import ch1_load_dict as load_dict
    import pandas as pd
    import numpy as np
    from itertools import combinations

    txt_file = load_dict.loader(path_to_dict)
    mystr = string.lower()
    comb = list(combinations(np.unique(list(mystr)), 2))
    comb_new = []

    for i in range(0, len(comb)):
        comb_new.append(list(comb[i]))
    
    table = pd.DataFrame({'Number of occurences': [0]*len(comb_new), 'Char pairs': comb_new})
    row = 0
    count = 0
    for i in comb:
        for j in set(txt_file):
            comb2 = list(combinations(list(j), 2))
            for k in comb2:
                if i == k:
                    table.iat[row,0] = count + 1
                    count = count + 1
        print(round(row/len(comb), 2))
        row = row + 1

    return table
    
print(occurence_count("Zwergkanadagans", "C:/Users/Lenovo/Desktop/STUDIA/IMPRACTICAL_PYTHON/example_dict.txt"))