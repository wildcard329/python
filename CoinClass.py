import random

class Coin:
    def __init__(self, result):
        self.r = result

    def __repr__(self):
        return '<Result: {}>'.format(self.r)
    
def cointoss():
    possibilities = ['Heads','Tails']
    c = Coin(result=random.choice(possibilities))
    print(c)

cointoss()
cointoss()
cointoss()
cointoss()
cointoss()
