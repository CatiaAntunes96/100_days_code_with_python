def ex_1():
    number = int(input())
    output = ""

    if number % 2 == 0:
        output = "even"
    else:
        output = "odd"

    print(f"This is an {output} number.")

def ex_2():
    height = float(input())
    weight = float(input())

    bmi = (weight / height ** 2)

    output = ""

    if bmi < 18.5:
        output = "underweight"
    elif  bmi < 25:
        output = "normal"
    elif  bmi < 30:
        output = "slighty overweight"
    elif  bmi < 35:
        output = "obese"
    else:
        output = "clinically obese"

    print(f"Your BMI is {bmi}, you are {output}")

def ex_3():
    year = int(input())
    output = ""

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            output = "Leap year"
        else:
            output = "Not Leap year"
    else:
        output = "Not Leap year"

    print(output)

def ex_4():
    print("Thank you for choosing Python Pizza Deliveries!")
    size = input("What size do you want?S, M or L ")

    if size not in ["S", "M", "L"]:
        print("Invalid Size")
        return
    add_pepperoni = input("Do you want pepperoni= Y or N ")

    if add_pepperoni not in ["Y", "N"]:
        print("Invalid Value")
        return

    extra_cheese = input("Do you want extra cheese? Y or N ")
    total = 0

    if extra_cheese not in ["Y", "N"]:
        print("Invalid Value")
        return

    if size == "S":
        total = 15
        if add_pepperoni == "Y":
            total += 2

    elif size == "M":
        total = 20
        if add_pepperoni == "Y":
            total += 3

    elif size == "L":
        total = 25
        if add_pepperoni == "Y":
            total += 3

    if extra_cheese == "Y":
        total += 1

    print(f"Your final bill is ${total}")

def ex_5():
    print("The Love Calculator is calculating your score...")
    name1 = input("What is your name? ").lower()
    name2 = input("What is your name? ").lower()

    total_true = 0
    total_love = 0

    for i in range(len(name1)):
        if name1[i] in ["t", "r", "u", "e"]:
            total_true += 1
        if name1[i] in ["l", "o", "v", "e"]:
            total_love += 1
    for i in range(len(name2)):
        if name2[i] in ["t", "r", "u", "e"]:
            total_true += 1
        if name2[i] in ["l", "o", "v", "e"]:
            total_love += 1
    total = int(str(total_true) + str(total_love))

    if total < 10 or total > 90:
        print(f"Your score is {total}, you go together like coke and mentos")
    elif 40 < total < 50:
        print(f"Your score is {total}, you are alright together")
    else:
        print(f"Your score is {total}")

def treasure_island():
    print("Welcome to treasure island")
    print("Your mission is to find the treasure")
    direction = input("You are at across road. Where do you want to go? Type 'left' or 'right' ")

    if direction == "left":
        action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the "
                       "boat. Type 'swim' to swim across ")
        if action == "swim":
            print("Game over")
            return
        action = input("Choose a color: 'red', 'yellow' or 'blue ")
        if action == "red" or action == "blue":
            print("Game over")
            return
        print("You win")
        return
    else:
        print("Game over")
        return

if __name__ == "__main__":
    treasure_island()