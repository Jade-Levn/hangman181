from random import choice

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please select a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
    check_guess(guess)
           

word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
word = choice(word_list)
print(word)

ask_for_input()