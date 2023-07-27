# display the occurences of characters in a string in a barplot manner
# QBA LIU 2023 -------------------------------------------------------------------------------------------------------------------------

def eng_char(string_in):
    import string
    import pprint
    letters_list = []

    for letter in string.ascii_lowercase:
        letters_list.append(letter)

    letters_dict = {}

    for i in letters_list:
        letters_dict[i] = []

    for key in letters_dict:
        for i in range(len(string_in)):
            if string_in[i].lower() == key:
                letters_dict[key].append(string_in[i])
    
    pp = pprint.PrettyPrinter(indent=4)
    return pp.pprint(letters_dict)


example_string = "Army backs coup as Niger president vows to protect democratic gains Reports Mohamed Bazoum being held by plotters, who earlier announced suspension of all state institutions"
print(eng_char(example_string))