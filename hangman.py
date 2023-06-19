import random
import string
from words import words

def get_valid_word(words):
    """Selects a valid word for the game.

    Parameters:
    - words (list): A list of words from which a valid word will be chosen.

    Returns:
    - str: A valid word chosen randomly from the list.

    This function selects a random word from the given list and ensures that
    the word does not contain any hyphens ('-').
    """

    word = random.choice(words)

    while "-" in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    """
       Implements the hangman game.

       This function runs the hangman game, where the player needs to guess a
       hidden word by suggesting letters.
       """

    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    print("Try a game of hangman. The goal is to guess the word before "
          "your lives ran out. ")

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        user_letter = input("Guess a letter: ").upper()

        print('You have used this letters: ', ' '.join(used_letters))

        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct",user_letter, "is part of the word.")
            else:
                lives = lives - 1
                print(user_letter,"isn't part of the word. You have", lives, "lives left.")

        elif user_letter in used_letters:
            print("You have already used that letter.")

        else:
            lives = lives - 1
            print("You entered an invalid charachter. Please try again.")

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", ' '.join(word_list))

    if lives == 0:
        print("Sorry, you ran out of lives. The correct answer was,",word)
    else:
        print("Congratulations!", word, "was the correct answer.")


hangman = hangman()
print(hangman)
