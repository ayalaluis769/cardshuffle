import itertools, random

# To make a deck of cards 
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

#To shuffle
random.shuffle(deck)

#To draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])