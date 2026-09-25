alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']


def refactor_position(p_position, p_cipher_type):
    if p_cipher_type == "e":
        while p_position > 25:
            p_position = p_position - 26
    else:
        while p_position < 0:
            p_position = p_position + 26
    return p_position


def caesar_cipher(p_initial_text, p_shift_number, p_cipher_type):
    pass


def encrypt(p_message, p_shift_number):
    cipher_message = ""

    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_shift_number
            while new_position >= 25:
                new_position = new_position - 26  
            new_char = alphabet[new_position]
            cipher_message += new_char
        else:
            cipher_message += char
    return f"The encoded message is {cipher_message}"


def decrypt(p_message, p_shift_number):
    message = ""

    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            old_position = position - p_shift_number 
            while old_position < 0:
                old_position = old_position + 26
            letter = alphabet[old_position]
            message += letter
        else: 
            message += char
    
    return f"The decoded message is: {message}"




end_program = False

while not end_program:
    encrypt_decrypt = input("Type 'E' to encrypt or type 'D' to decrypt:\n").lower()
    message = input("Enter your message?\n").upper()
    shift_number = int(input("Enter the shift number:\n"))

    if encrypt_decrypt == "e":
        enc_message = encrypt(message, shift_number)
        print(enc_message)
    elif encrypt_decrypt == "d":
        dec_message = decrypt(message, shift_number)
        print(dec_message)
    else: 
        print("Choose E or D")

    restart = input("Type 'Y' if you want to continue, Otherwise type 'Q: ").lower()
    if restart == 'n':
        end_program = True
        print("See you next time")
    else:
        continue
