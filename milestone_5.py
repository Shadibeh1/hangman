import random


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

        print(f"Welcome to Hangman! Guess the word: {' '.join(self.word_guessed)}")
        print(f"You have {self.num_lives} lives remaining.")

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
            return

        self.list_of_guesses.append(guess)

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(f"Word: {' '.join(self.word_guessed)}")
            self.num_letters -= 1
        else:
            print(f"Bad luck! '{guess}' is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives remaining.")
            print(f"Word: {' '.join(self.word_guessed)}")

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            else:
                self.check_guess(guess)
                if self.num_lives <= 0:
                    break
                if self.num_letters == 0:
                    break


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives <= 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break


if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    play_game(word_list)