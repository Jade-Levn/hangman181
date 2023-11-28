from random import choice

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word_guessed = []
        
        self.num_letters = len(set(word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        
        for index, letter in enumerate(word):
            if letter == guess:                
                self.word_guessed[index] = guess
                print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        for i in range(len(word)):
            self.word_guessed.append('_')
        print(self.word_guessed)

        while True:
            guess = input("Please guess a letter: ")
            #if len(guess) == 1 and guess.isalpha():
                #break
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def play_game(self, word_list):
        self.num_lives = 5
        game = Hangman(word_list, num_lives)

        while True:
            if self.num_lives == 0:
                print("You lost!")
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")


word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
word = choice(word_list)

play_game(word_list)
print(word)