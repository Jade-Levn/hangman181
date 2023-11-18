while True:
    guess = input("Please select a letter: ")
    if len(guess) == 1 and guess.isalpha():
        guess = guess.lower()
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")