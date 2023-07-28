import sys

def loader(file_in):
    try:
        with open(file_in) as file:
            txt = file.read().strip().split('\n')       # convert txt file to list
            txt = [element.lower() for element in txt]  # convert every character in list to lowercase
            return txt
    except IOError:
        print("Error opening file {}".format(file_in), file = sys.stderr)


#print(loader("C:/Users/Lenovo/Desktop/STUDIA/IMPRACTICAL_PYTHON/example_dict.txt"))