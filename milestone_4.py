from random import choice

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word_guessed = []
        
        num_letters = len(set(word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        """
        for letter in word:
            if letter == guess:
                current_index = word.index(letter)
                #print(current_index)
                print(f"{letter} is at = index: {current_index}")
                self.word_guessed[current_index] = guess
                print(self.word_guessed)
        """
        for index, letter in enumerate(word):
            if letter == guess:
                print(f"{letter} is at = index: {index}")
                
                self.word_guessed[index] = guess
                print(self.word_guessed)


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
        

        

word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
word = choice(word_list)
print(word)

game = Hangman(word_list)
game.ask_for_input()

"""Task 3 implementation:
Return to your check_guess method and extend it to replace the underscore(s) in the word_guessed with the letter guessed by the user.
In the if block of your check_guess method, after your print statement, do the following:

Create a for-loop that will loop through each letter in the word /
Within the for-loop, do the following:
Create an if statement that checks if the letter is equal to the guess /
In the if block, replace the corresponding "_" in the word_guessed with the guess. HINT: You can index the word_guessed at the position of the letter and assign it to the letter
Outside the for-loop, reduce the variable num_letters by 1
"""