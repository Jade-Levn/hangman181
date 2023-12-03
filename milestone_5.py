from random import choice

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = choice(word_list)
        #print(self.word)
        
        self.word_guessed = []
        
        for i in range(len(self.word)):
            self.word_guessed.append('_')
        print(self.word_guessed)
        
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        This method checks to see if a player's guess is within the selected word.

        If the guess is in the word, the underscore is replaced with the correct letter.
        If the guess is incorrect, the player loses a life.
        Argument:
            guess: a string.
        Returns: 
            None.
        """
        guess = guess.lower()
        
        if guess in self.word:                
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(self.word_guessed)
            

    def ask_for_input(self):
        """
        This method asks the player for input.

        Checks if a user's guess is a single, alphabetical letter.
        Returns: 
            None.
        """
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f"List of guesses: {self.list_of_guesses}")
                print(f"Num list of guesses: {len(self.list_of_guesses)},\nNum list of letters: {self.num_letters}")
                if self.num_lives == 0:
                    break
                elif "_" not in self.word_guessed:
                    break
            

def play_game(word_list):
    """
    This function runs the Hangman game.

    Creates an instance of the class Hangman. Contains win conditions for the game.
    Returns: 
        None.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(f"Number of letters left: {game.num_letters}")
            game.ask_for_input()
            continue
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        else:
            print("An error has occurred.")
            break

word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
play_game(word_list)