import random


def hangman():
    word_list = ["ardvark", "baboon", "camel"]

    random_word = random.choice(word_list)

    display = []
    lives = 3
    points = len(random_word)

    for letter in random_word:
        display.append("_")
    print(display)

    while lives > 0 and points > 0:
        guess = input("Make a guess: ").lower()
        match_letter = False
        for i in range(len(random_word)):
            if guess == random_word[i]:
                print("Right")
                display[i] = guess
                points -= 1
                match_letter = True
            else:
                print("Wrong")

        if not match_letter:
            lives -= 1
        print(display)
        print(f"Points: {points}")
        print(f"Lives: {lives}")

    if points == 0:
        print("You win")
    else:
        print("Game over")

if __name__ == "__main__":
    hangman()