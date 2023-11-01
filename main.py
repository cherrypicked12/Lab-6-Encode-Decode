# Alice Jiang

def encode(password):
    encoded_pass = ""
    for num in range(0, len(password)):
        encoded_num = str(int(password[num]) + 3)
        if len(encoded_num) == 2:
            encoded_num = encoded_num[1:]
        encoded_pass += encoded_num
    return encoded_pass


# Tanushree Hadavale

# Tanushree
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

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = str(input("Please enter your password to encode: "))
            encode_pass = encode(password)
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            decode_pass = decode(encode_pass)
            print(f"The encoded password is {encode_pass}, and the original password is {decode_pass}.")
        elif user_input == 3:
            break


if __name__ == "__main__":
    main()