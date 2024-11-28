import random
from Poker_classes import *
   

starting_chips = 100

deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

random.shuffle(deck)

p1 = Player([deck[0],deck[2]],starting_chips,0)
p2 = Player([deck[1],deck[3]],starting_chips,0)
deck = deck[4:]

Dealer = Dealer([],0,deck)


print("Player 1 Hand: " + p1.get_hand()[0] + ", " + p1.get_hand()[1])
print("Player 2 Hand: " + p2.get_hand()[0] + ", " + p2.get_hand()[1])


Dealer.deal_flop()
print(Dealer.get_table())

    
    
        
        