def encode_password(password):
    """Encode an 8-digit password by shifting each digit up by 3"""
    encoded = ""
    for digit in password:
        encoded += str((int(digit) + 3) % 10)
    return encoded


def decode_password(encoded):
    """Decode an encoded password by shifting each digit down by 3"""
    password = ""
    for digit in encoded:
        password += str((int(digit) - 3) % 10)
    return password



while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded = encode_password(password)
        print("Your password has been encoded and stored!")
    elif choice == "2":
        if not encoded:
            print("Error: no encoded password has been stored yet")
        else:
            password = decode_password(encoded)
            print(f"The encoded password is {encoded}, and the original password is {password}.")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please enter 1, 2, or 3.")