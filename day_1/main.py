def ex_1():
    print("""Day 1 - Python Print Function
    The function is declared like this:
    print('what to print')""")


def ex_2():
    print(len(input()))


def ex_3():
    a = input()
    b = input()

    aux = a
    a = b
    b = aux

    print(f"a: {a}")
    print(f"b: {b}")


def band_generator():
    print("Welcome to the Band Name Generator.\n")
    city = input("What's name of the city you grew up in?")
    pet_name = input("What's your pet's name?")
    print(f"Your band name could be {city} {pet_name}")


if __name__ == "__main__":
    band_generator()
