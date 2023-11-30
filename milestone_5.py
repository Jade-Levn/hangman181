from random import choice

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = choice(word_list)
        print(self.word)
        
        self.word_guessed = []
        
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
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        for i in range(len(self.word)):
            self.word_guessed.append('_')
        print(self.word_guessed)

        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                #break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")


word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
#game = Hangman(word_list)
#game.ask_for_input()
#word = choice(word_list)

play_game(word_list)
#print(word)