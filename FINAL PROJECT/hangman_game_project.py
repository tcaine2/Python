# FILE NAME - hangman_game_project.py

# NAME: Thomas Caine
# DATE: 12/8/24

import random

def load_words(game_words):
    file = open('game_words.txt', 'r')
    words = []
    for line in file:
        line = line[:-1] if line[-1] == '\n' else line
        words.append(line)
    file.close()
    return words

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed[:-1]

def main():
    play_hangman()

def play_hangman():
    words = load_words("game_words.txt")
    word = random.choice(words).lower()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.\n")

    while attempts_left > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts_left}")

        letter_guess = input("Guess a letter: ").lower()

        guessed_letters.append(letter_guess)

        if letter_guess in word:
            print(f"Good guess! {letter_guess} is in the word.")
        else:
            print(f"Wrong guess! {letter_guess} is not in the word.")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            return

    print(f"\nGame Over Man!!! The word was: {word}")

play_hangman()

main()
