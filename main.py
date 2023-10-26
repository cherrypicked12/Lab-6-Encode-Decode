# Alice Jiang

def encode(password):
    encoded_pass = ""
    for num in range(0, len(password)):
        encoded_num = str(int(password[num]) + 3)
        if len(encoded_num) == 2:
            encoded_num = encoded_num[1:]
        encoded_pass += encoded_num
    return encoded_pass
