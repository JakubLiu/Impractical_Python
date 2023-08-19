"""
The code below ecnrypts a message in the following way.

For example, to encrypt the message 'WE ARE DISCOVERED. RUN AT ONCE.' with 3 "rails", write the text as:

W . . . E . . . C . . . R . . . U . . . O . . . 
. E . R . D . S . O . E . E . R . N . T . N . E 
. . A . . . I . . . V . . . D . . . A . . . C . 
(Note that spaces and punctuation are omitted.) Then read off the text horizontally to get the ciphertext:

WECRUO ERDSOEERNTNE AIVDAC

QBA LIU 2023 -----------------------------------------------------------------------------------------------------------------------
"""
import string

plaintext = "We are discovered. Run at once."

def main():
    step1 = text_prep(plaintext)
    step2 = rail_maker(step1)
    step3 = five_cutter(step2)
    print(step3)

def text_prep(raw_text):
    text_out = raw_text.translate(str.maketrans('', '', string.punctuation))
    text_out = ''.join(text_out.split())
    text_out = text_out.upper()
    return text_out


def rail_maker(text_in, rails = False, encryption = True):
    rail1 = text_in[::4]
    rail2 = text_in[1::2]
    rail3 = text_in[2::4]
    message_encrypt = rail1 + rail2 + rail3
    
    if rails == True:
        return rail1, rail2, rail3

    elif encryption == True:
        return message_encrypt

def five_cutter(message):
    words = []
    for i in range(0, len(message), 5):
        words.append(message[i:i+5])
    
    final_encryption = " ".join(words)
    return final_encryption

if __name__ == "__main__":
    main()