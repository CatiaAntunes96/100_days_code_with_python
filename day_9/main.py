import random

from replit import clear


def ex_1():
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62
    }

    student_grades = {}
    for name in student_scores:
        grade_description = ""
        if student_scores[name] > 90:
            grade_description = "Outstanding"
        elif student_scores[name] > 80:
            grade_description = "Exceeds Expectations"
        elif student_scores[name] > 70:
            grade_description = "Acceptable"
        else:
            grade_description = "Fail"

        student_grades[name] = grade_description

    print(student_grades)


def ex_2():
    country = input("Add country name: ")
    visits = input("Number of visits: ")
    list_of_cities = eval(input("List"))

    travel_log = [{
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    }, {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }, add_new_country(country, visits, list_of_cities)]

    print(travel_log)


def add_new_country(country, visits, list_of_cities):
    new_entry = {}
    new_entry["country"] = country
    new_entry["visits"] = visits
    new_entry["cities"] = list_of_cities

    return new_entry


def secret_auction():
    print("Welcome to the secret auction program")
    add_bidders = True
    all_bids = []

    while add_bidders:
        name = input("What is your name? ")
        bid = input("What's your bid? ")

        all_bids.append(add_new_bid(name, bid))

        add_new_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

        if add_new_bidder == 'no':
            add_bidders = False
        else:
            clear()

    max_bidder = all_bids[0]

    for bidder in all_bids:
        if int(bidder["bid"]) > int(max_bidder["bid"]):
            max_bidder = bidder

    print(f"Te winner is {max_bidder['name']} with {max_bidder['bid']} ")


def add_new_bid(name, bid):
    new_bid = {}
    new_bid["name"] = name
    new_bid["bid"] = bid

    return new_bid


if __name__ == "__main__":
    secret_auction()
