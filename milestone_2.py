#from random import choice - this works but for the purpose of the project...
import random

word_list = ["pineapple", "mango", "grapes", "strawberries", "kiwi"]
#print(word_list)

#word = choice(word_list) - this works but for the purpose of the project...
word = random.choice(word_list)

for num in range(5):
    word = random.choice(word_list)
    print(word)