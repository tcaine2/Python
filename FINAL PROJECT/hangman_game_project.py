# FILE NAME - hangman_game_project.py

# NAME: Thomas Caine
# DATE: 12/8/24

import random
import time

def insert_words(game_words):
    file = open('/workspaces/Python/FINAL PROJECT/game_words.txt', 'r')
    words = []
    for line in file:
        words.append(line.strip())
    file.close()
    return words

def display_word(word, guessed_letters):
    displayed_letter = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_letter += letter + " "
        else:
            displayed_letter += "_ "
    return displayed_letter

def play_again():
    while True:
        replay = input("Would you like to play again? (y/n): ")
        if replay == "y":
            return True
        elif replay == "n":
            print("\nThanks for playing! Goodbye!")
            return False

def main():
    while True:
        random.seed(time.time())
        words = insert_words('/workspaces/Python/FINAL PROJECT/game_words.txt')
        input_word = random.choice(words)
        guessed_letters = []
        attempts_left = 6

        print("\nWelcome to Hangman!\n")
        print("Rules of the game:\n1. Try to guess the word below\n2. Guess the word one letter at a time\n3. All letters you guess must be lowercase\nGood luck!")

        while attempts_left > 0:
            print("\n" + display_word(input_word, guessed_letters))
            print(f"Guessed letters: {guessed_letters}")
            print(f"Attempts left: {attempts_left}")

            letter_guess = input("Guess a letter: ")

            if letter_guess in guessed_letters:
                print(f"\nYou already guessed '{letter_guess}'. Try again!")
                continue

            guessed_letters.append(letter_guess)

            if letter_guess in input_word:
                print(f"\nGood guess! {letter_guess} is in the word.")
            else:
                print(f"\nWrong guess! {letter_guess} is not in the word.")
                attempts_left -= 1

            all_letters_guessed = True
            for letter in input_word:
                if letter not in guessed_letters:
                    all_letters_guessed = False
                    break

            if all_letters_guessed:
                print(f"\nCongratulations! You guessed the word: {input_word}")
                break

        else:
            print(f"\nGame Over Man!!! The word was: {input_word}\n")

        if not play_again():
            break

main()
