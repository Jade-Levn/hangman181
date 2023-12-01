from random import choice

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = choice(word_list)
        
        self.word_guessed = []
        
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def play_game(self):
        num_lives = 5

        game = Hangman(word_list, num_lives)
        print(game.word)
        #game.word_list = self.word_list
    
        print(f"Game number of lives: {game.num_lives}\nSelf number of lives: {self.num_lives}")
        print(f"Game number of letters: {game.num_letters}\nSelf number of letters: {self.num_letters}")
        #game.num_lives = self.num_lives
        #game.num_letters = self.num_letters

        while True:
            #print("Help!")
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_letters > 0:
                print(f"Number of letters left: {game.num_letters}")
                game.ask_for_input()
                break
            else:
                print("Congratulations. You won the game!")
                break
            #False
        
        #print(f"Game number of lives: {game.num_lives}\n Self number of lives: {self.num_lives}")
        #print(f"Game number of letters: {game.num_letters}\n Self number of letters: {self.num_letters}")

    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:                
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
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]

hangman = Hangman(word_list)
#hangman.play_game(word_list)
hangman.play_game()