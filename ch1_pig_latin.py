# QBA LIU 2023 -----------------------------------------------------------------------------------------------------------------------

def vowel_check(char):
# check if a character is a vowel or not
# return 0 if character is not a vowel
# return 1 if character is a vowel
    out = 0
    vowels = ['a', 'e', 'o', 'u', 'i']
    
    for i in vowels:
        if i == char.lower():
            out = 1
    
    return out

def pig_latin(word):
    if vowel_check(word[0]) == 0:
        word_new = word[1:] + word[0] + 'ay'
    else:
        word_new = word + 'way'
    return word_new

print(pig_latin('Jula'))