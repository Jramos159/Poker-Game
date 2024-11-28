class Player:
    def __init__(self,HAND,CHIP_COUNT,BET_COUNT):
        self.HAND = HAND
        self.CHIP_COUNT = CHIP_COUNT
        self.BET_COUNT = BET_COUNT
        
    def get_hand(self):
        return self.HAND
        
class Dealer:
    def __init__(self,TABLE, POT, DECK):
        self.TABLE = TABLE
        self.POT = POT
        self.DECK = DECK
        
    def get_table(self):
        return self.TABLE
    
    def deal_flop(self):
        self.TABLE = self.DECK[:2]
        self.DECK = self.DECK[2:]
        
        
        
        
        