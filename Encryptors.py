import math as m
from random import randint

def Encrypt_Cezar(text = "abc", key = 777):
    ''' doc-strign: Encrypt_Cezar is a function takes 1 argument string, and returns text encrypted by Cezar. If no argument passed, default argument  = "abc" Rot 1'''
    # get text from textfield
    encrypted_str = text
    if key == 777:
        key = randint(1,26)

    result = ""

    # traverse text
    for i in range(len(encrypted_str)):
        char = encrypted_str[i]

        # Shift (uppercase characters)
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)

        # Shift (lowercase characters)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result, key

# ---- test test test ---------
if __name__ == "__main__":
    Encrypt_Cezar("a")
else:
    pass