"""
This programme hides a message in a list of words. The names Stuard and Jacob are obligatory and do not hide any letters.
Their purpose is to disguise the hidden message.
Example:
'Help'
Ghana, Stuard, Edd, Client, Jacob, Pig
QBA LIU 2023 -------------------------------------------------------------------------------------------------------------------
"""
import ch1_load_dict as load
import string
# a list that holds all the necessary words
names_list = load.loader("C:/Users/Lenovo/Desktop/STUDIA/IMPRACTICAL_PYTHON/supporters.txt")
message = 'Give me your word and we rise'


def message_prep(message_raw):
    message_out = ''.join(message_raw.split())
    message_out = message_out.lower()
    return message_out


def hide(message_in, names):

    names_out = [None] * len(message_in)
    pos = 1
    idx = 0
    Stuard_idx = 5
    Jacob_idx = 14
    names_out[Stuard_idx] = 'Stuard'
    names_out[Jacob_idx] = 'Jacob'


    for char_mess, point in zip(message_in, names_out):             # iterate over letters in message
        for name in names:
            if pos%2 == 0 and point != 'Stuard' and point != 'Jacob':
                if name[1] == char_mess:                # if second lettter of name is equal current letter in message
                    names_out[idx] = [name, pos%2]
                    break
            elif pos%2 != 0 and point != 'Stuard' and point != 'Jacob':                            # if third lettter of name is equal current letter in message
                if name[2] == char_mess:
                    names_out[idx] = [name,pos%2]
                    break
            elif point == 'Stuard':
                Stuard_idx2 = idx + 1
                break
            elif point == 'Jacob':
                Jacob_idx2 = idx + 1
                break
        pos = pos + 1
        idx = idx + 1

    names_out[Stuard_idx2] = 'loc1'
    names_out[Jacob_idx2] = 'loc2'

    for name_out in names_out:
        if name_out == 'loc1':

           if names_out[names_out.index(name_out) - 2][1] == 0:
                
                char_idx = 0
                for char_mess in message_in:
                    if char_idx == Stuard_idx:
                        for name in names:
                            if len(name) > 3:
                                if name[2] == message_in[char_idx]:
                                    names_out[char_idx+1] = [name, 1]
                    char_idx = char_idx + 1

           elif names_out[names_out.index(name_out) - 2][1] == 1:

                char_idx = 0
                for char_mess in message_in:
                    if char_idx == Stuard_idx:
                        for name in names:
                            if len(name) > 3:
                                if name[1] == message_in[char_idx]:
                                    names_out[char_idx+1] = [name, 1]
                    char_idx = char_idx + 1
        
        elif name_out == 'loc2':
            
            if names_out[names_out.index(name_out) - 2][1] == 0:

                char_idx = 0
                for char_mess in message_in:
                    if char_idx == Jacob_idx:
                        for name in names:
                            if len(name) > 3:
                                if name[2] == message_in[char_idx]:
                                    names_out[char_idx+1] = [name, 1]
                    char_idx = char_idx + 1

            elif names_out[names_out.index(name_out) - 2][1] == 1:
                
                char_idx = 0
                for char_mess in message_in:
                    if char_idx == Jacob_idx:
                        for name in names:
                            if len(name) > 3:
                                if name[1] == message_in[char_idx]:
                                    names_out[char_idx+1] = [name, 1]
                    char_idx = char_idx + 1


            names_out[Stuard_idx] = ['Stuard', 1]
            names_out[Jacob_idx] = ['Jacob', 1]


        names_out_final = []
        for i in names_out:
            names_out_final.append(i[0])
                
    return names_out_final

    
print(message)
print(hide(message_in=message_prep(message), names = names_list))
