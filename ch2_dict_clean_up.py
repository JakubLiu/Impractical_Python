# script to remove single letter words from a dictionary
# QBA LIU 2023 -----------------------------------------------------------------------------------------------------------------

import ch1_load_dict as load_dict  # import ch1_load_dict.py (has to be in the same directory)

file_orig = load_dict.loader("C:/Users/Lenovo/Desktop/STUDIA/IMPRACTICAL_PYTHON/example_dict.txt")  # use a function from the importet programme
file_new = []

# clean up
for i in file_orig:
    if len(i) > 1:
        file_new.append(i)

# compare sizes
print(len(file_orig))
print(len(file_new))