import random

words = ["python", "coding", "shadow"]
word = random.choice(words)

guessed = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("You Win!")
        break

    guess = input("Enter letter: ")

    if guess not in word:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    guessed.append(guess)

if attempts == 0:
    print("You Lose! Word was:", word)