import string

file_in = "C:/Users/Lenovo/Desktop/STUDIA/IMPRACTICAL_PYTHON/hidden_help_message.txt"

def message_prep(file_in):

    with open(file_in) as file:
        hidden_message = file.read().split()
        hidden_message_clean = []

        for word in hidden_message:
            for char in word:
                if char not in string.ascii_letters:
                    word = word.replace(char, '')
            hidden_message_clean.append(word)
    
        return hidden_message_clean

message = message_prep(file_in=file_in)

def decipher(hidden_message, n):
    message_out = []

    for i in range(0, len(hidden_message) + 1, n):
        letter = hidden_message[i][n-1]             # n - 1 because Python is zero based
        letter = letter.upper()
        message_out.append(letter)

    return message_out


print('Original message:', '\n', message, '\n', 'Deciphered message:', '\n', decipher(message, 2))