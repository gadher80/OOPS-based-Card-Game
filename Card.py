#CARD
# RANK, VALUE, SUIT
import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):

        self.allcards = []

        for suit in suits:
            for rank in ranks:

                created_card = Card(suit,rank)
                self.allcards.append(created_card)

    def shuffle(self):

        random.shuffle(self.allcards)

    def deal_one(self):

        return self.allcards.pop()

if __name__ == '__main__':


    new_deck = Deck()
    new_deck.shuffle()

    mycard = new_deck.deal_one()
    print(mycard)

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


if __name__ == '__main__':

    New_player = Player('Hardik')

    New_player.add_cards(mycard)

    New_player.add_cards([mycard,mycard,mycard])

    New_player.remove_one()

    print(New_player)
