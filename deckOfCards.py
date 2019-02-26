import random

class Card:
    def __init__(self, value, suit):
        self.v = value
        self.s = suit

    def __repr__(self):
        return '<Card: {} of {}>'.format(self.v, self.s)
    

def draw():
    suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    value = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    x = Card(value=random.choice(value),suit=random.choice(suit))
    print(x)

draw()
draw()
draw()
draw()
draw()
