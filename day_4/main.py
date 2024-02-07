import random


def ex_1():
    rand_number = random.randint(0, 1)

    if rand_number == 1:
        print("Heads")
    else:
        print("Tails")

def ex_2():
    names_string = input()
    names = names_string.split(", ")

    rand = random.randint(0, len(names))

    print(names[rand])

def game():
    player = int(input())

    moves = ["rock", "paper", "scissors"]

    rand = random.randint(0, 2)
    game = moves[rand]
    print(moves[player])
    print(game)

    if moves[player] == game:
        print("No one wins")
    elif game == "rock":
        if moves[player] == "paper":
            print("You win")
        if moves[player] == "scissors":
            print("You lose")
    elif game == "paper":
        if moves[player] == "rock":
            print("You lose")
        if moves[player] == "scissors":
            print("You win")
    elif game == "scissors":
        if moves[player] == "paper":
            print("You lose")
    if moves[player] == "rock":
        print("You win")


if __name__ == "__main__":
    game()