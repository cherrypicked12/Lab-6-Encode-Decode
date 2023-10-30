# Alice Jiang

def encode(password):
    encoded_pass = ""
    for num in range(0, len(password)):
        encoded_num = str(int(password[num]) + 3)
        if len(encoded_num) == 2:
            encoded_num = encoded_num[1:]
        encoded_pass += encoded_num
    return encoded_pass

def decode(encoded_pass):
    decoded_pass = []
    for num in encoded_pass:
        new_num = int(num) - 3                 # Subtracts 3 from every number in the encoded password
        if new_num in range(-3, 0):            # If the result of the subtraction is negative, the decoded new_num
            if new_num == -3:                  # is changed to its correct value
                new_num = 7
            elif new_num == -2:
                new_num = 8
            elif new_num == -1:
                new_num = 9
        decoded_pass.append(str(new_num))
    decoded_pass = ''.join(decoded_pass)       # Changes the decoded_pass list into a string
    return decoded_pass

