from random import choice

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        #num_lives = 5
        self.num_lives = num_lives

        self.word = choice(word_list)
        print(self.word)
        
        self.word_guessed = []
        
        for i in range(len(self.word)):
            self.word_guessed.append('_')
        print(self.word_guessed)
        
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:                
            #self.word_guessed[index] = guess
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            #num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(self.word_guessed)

    def ask_for_input(self):

        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    print(f"Game number of lives 1: {game.num_lives}")
    print(f"Game number of letters 1: {game.num_letters}")

    while True:
        #print(f"Number of lives = {game.num_lives}")
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(f"Number of letters left: {game.num_letters}")
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

        print(f"Game number of lives 2: {game.num_lives}")
        print(f"Game number of letters 2: {game.num_letters}")

word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]

play_game(word_list)