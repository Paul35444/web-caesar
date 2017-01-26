def aplhabet_position(letter):
    if len(letter) != 1:
        return 0
    new = ord(letter)
    if 65 <= new <= 90: #Upper case letters 65 to 90
        return new - 64
    elif 97 <= new <= 122: #Lower case letter 97 to 122
        return new - 96
    return 0

def rotate_character(message, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherText = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                caps = True
            else:
                caps = False
            alphabet = ord(c.lower()) + rot
            if alphabet > ord('z'):
                alphabet -= 26
            letter = chr(alphabet)
            if caps is True:
                letter = letter.upper()
            cipherText += letter
        else:
            cipherText += c
    return cipherText

def encryption(plaintext, key):
    text_len = len(plaintext)
    key *= text_len // len(key) + 1
    key = key[:text_len]

    encoded = ""

    for c in range(text_len):
        newchar = ord(plaintext[c]) + ord(key[c]) - 194
        newchar %= 25
        encoded += chr(newchar + 97)
    return encoded
