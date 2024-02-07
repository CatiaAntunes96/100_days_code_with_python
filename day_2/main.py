def ex_1():
    height = float(input())
    weight = float(input())

    bmi = weight / (height * height)

    print(int(bmi))


def ex_2():
    age = int(input())

    years_left = 90 - age

    weeks_left = years_left * 52

    print(f"You have {weeks_left} weeks left.")


def tip_calculator():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? "))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

    if tip_percentage not in [10, 12, 15]:
        print("Invalid percentage")
        return

    tip_percentage = tip_percentage / 100
    total_people = int(input("How many people to split the bill? "))
    total_bill += (total_bill * tip_percentage)
    total_by_person = round(total_bill / total_people, 2)

    print(f"Each person should pay: {total_by_person}")


if __name__ == "__main__":
    tip_calculator()
