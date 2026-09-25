alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']


message = input("What do you want to encrypt?\n").upper()
shift_number = int(input("Enter the shift number:\n"))
    

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

encoded_message = encrypt(message, shift_number)
print(encoded_message)