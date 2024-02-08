import math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']


def paint_area_calculator():
    test_h = int(input("Height of Wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5

    total_cans = paint_area_calc(height=test_h, width=test_w, coverage=coverage)
    print(f"You'll need {total_cans} cans of paint.")


def paint_area_calc(height, width, coverage):
    return math.ceil((height * width) / coverage)


def is_prime_number():
    number = int(input("Check this number: "))
    is_prime = prime_number_checker(number)
    if is_prime:
        print("It's a prime number")
    else:
        print("Not a prime number")


def prime_number_checker(number):
    temp = 0

    for i in range(2, math.ceil(number / 2)):
        if number % i == 0:
            temp += 1
            break
        i += 1

    return True if temp == 0 and number != 1 else False


def ceaser_cypher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if direction == "encode":
        message_encrypted = encrypt(message, shift)
        print(f"The encoded text is {message_encrypted}")
    elif direction == "decode":
        message_decrypted = decrypt(message, shift)
        print(f"the decoded text is {message_decrypted}")


def encrypt(text, shift):
    cyper_text = ""
    for letter in text:
        index = letters.index(letter)
        index_to_shift = index + shift
        if index_to_shift >= len(letters):
            remaining_shift = index_to_shift - (len(letters)-1)
            index_to_shift = remaining_shift
        cyper_text += letters[index_to_shift]

    return cyper_text


def decrypt(text, shift):
    cyper_text = ""
    for letter in text:
        index = letters.index(letter)
        index_to_shift = index - shift
        if index_to_shift < 0:
            remaining_shift = (len(letters)-1) + index_to_shift
            index_to_shift = remaining_shift
        cyper_text += letters[index_to_shift]

    return cyper_text


if __name__ == "__main__":
    ceaser_cypher()
