import random


words = ["apple", "banana", "grape", "orange", "mango"]
secret_word = random.choice(words)


def check_guess(guess):
    """
    Check if the guessed letter is in the secret word.

    Args:
        guess (str): The guessed letter.

    Returns:
        None

    """

    guess = guess.lower()

    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")


def ask_for_input():
    while True:

        guess = input("Guess a letter: ").lower()
        if len(guess) == 1:
            check_guess(guess)

        else:
            print('invalid')

ask_for_input()


