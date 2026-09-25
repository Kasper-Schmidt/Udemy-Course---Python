alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']


message = input("What do you want to encrypt?\n").upper()
shift_number = int(input("Enter the shift number:\n"))

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

decrypted = decrypt(message, shift_number)
print(decrypted)