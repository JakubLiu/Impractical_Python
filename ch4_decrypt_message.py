"""
The code below decrypts a message ecrypted by the following encryption method.

To encrypt the message 'WE ARE DISCOVERED. RUN AT ONCE.' with 3 "rails", write the text as:

W . . . E . . . C . . . R . . . U . . . O . . . 
. E . R . D . S . O . E . E . R . N . T . N . E 
. . A . . . I . . . V . . . D . . . A . . . C . 
(Note that spaces and punctuation are omitted.) Then read off the text horizontally to get the ciphertext:

WECRUO ERDSOEERNTNE AIVDAC

QBA LIU 2023 -------------------------------------------------------------------------------------------------------------------------
"""

import ch4_encrypt_message as encrypt
import math

# function to remove whitespaces
def space_remover(message_encrypt):
    message = "".join(message_encrypt.split())
    return message

# function to check for eveness
def even(num):
    out = 1    # return 1 if number is even, return 0 if number is odd
    if num%2 != 0:
        out = 0
    return out

# function to substract two strings from eachother
def string_substract(stringA, stringB):
    out = stringA.rsplit(stringB)
    
    if out[0] != '':
        return out[0]
    else:
        return out[1]


# function to create rails
def rail_remaker(message):
    len_message = len(message)

    if even(len_message) == 1:
        len_rail2 = int(len_message/2)
        other_rail_lengths = len_message - len_rail2

        if even(other_rail_lengths) == 1:
            len_rail1 = int(len_message/4)
            len_rail3 = int(len_message/4)
        else:
            len_rail1 = math.floor(other_rail_lengths/2) + 1
            len_rail3 = math.floor(other_rail_lengths/2)
    
    else:
        len_rail2 = int(len_message/2 - 0.5)
        other_rail_lengths = len_message - len_rail2

        if even(other_rail_lengths) == 1:
            len_rail1 = int(other_rail_lengths/2)
            len_rail3 = int(other_rail_lengths/2)

        else:
            len_rail1 = math.floor(other_rail_lengths/2) + 1
            len_rail3 = math.floor(other_rail_lengths/2)
    
    rail1 = message[:len_rail1]
    rail3 = message[len_message-len_rail3:]
    rail2_raw = string_substract(message, rail1)
    rail2 = string_substract(rail2_raw, rail3)

    return rail1, rail2, rail3

# function to decode the information written in the rails
def rail_decoder(rails):

    rail1 = list(list(rails)[0])
    rail2 = list(list(rails)[1])
    rail3 = list(list(rails)[2])
    list_out = [None] * (len(rail1) + len(rail2) + len(rail3))

    count_r1 = 0
    for r1 in rail1:
        list_out[count_r1] = r1
        count_r1 = count_r1 + 4


    count_r2 = 1
    for r2 in range(0, len(rail2), 2):
        list_out[count_r2] = rail2[r2]
        count_r2 = count_r2 + 4

    count_r3 = 2
    for r3 in rail3:
        list_out[count_r3] = r3
        count_r3 = count_r3 + 4

    count_r2_v2 = 3
    for r2 in range(1, len(rail2), 2):
        list_out[count_r2_v2] = rail2[r2]
        count_r2_v2 = count_r2_v2 + 4

    out = ''.join(list_out)
    return out

original_message = 'Expect heavy rainfall in two days time'
coding1 = encrypt.text_prep(original_message)
coding2 = encrypt.rail_maker(coding1)
code = encrypt.five_cutter(coding2)
removed_space = space_remover(code)
new_rails = rail_remaker(removed_space)
decoded = rail_decoder(new_rails)
print('original message: ', original_message)
print('coded message: ', code)
print('decoded message: ',decoded)
