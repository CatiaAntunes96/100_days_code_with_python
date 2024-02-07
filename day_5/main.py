import random


def ex_fizz():
    for i in range(1, 100 + 1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def password_generator():
    total_letters = int(input("How many letters? "))
    total_symbols = int(input("How many symbols? "))
    total_numbers = int(input("How many numbers? "))

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '!', '#', '$', '&', '%', '?', '=', '^', '~']
    password = ""

    total_length = total_letters + total_symbols + total_numbers

    while len(password) != total_length:
        if total_letters > 0:
            ran_letter = random.randint(0, len(letters))
            print(f"Letter is {ran_letter}")
            password += (letters[ran_letter])
            total_letters -= 1

        if total_numbers > 0:
            ran_number = random.randint(0, len(numbers))
            print(f"Number is {ran_number}")
            password += (numbers[ran_number])
            total_numbers -= 1
        if total_symbols > 0:
            ran_symbols = random.randint(0, len(symbols))
            print(f"Symbol is {ran_symbols}")
            password += (symbols[ran_symbols])
            total_symbols -= 1

    print(f"Your password is {password}")


if __name__ == "__main__":
    password_generator()
