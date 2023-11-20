from random import choice

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        word_guessed = []
        for i in range(len(word)):
            word_guessed.append('_')
        print(word_guessed)
        
        num_letters = len(set(word))
        #list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")


    def ask_for_input(self):
        list_of_guesses = []
        while True:
            guess = input("Please guess a letter: ")
            #if len(guess) == 1 and guess.isalpha():
                #print()
                #break
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                list_of_guesses.append(guess)

word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
word = choice(word_list)
print(word)

game = Hangman(word_list)
game.ask_for_input()