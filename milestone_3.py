from random import choice

word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
word = choice(word_list)
#print(word)

while True:
    guess = input("Please select a letter: ")
    if len(guess) == 1 and guess.isalpha():
        guess = guess.lower()
        
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        break
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
