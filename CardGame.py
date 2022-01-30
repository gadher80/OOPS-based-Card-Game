# sourcery skip: aug-assign, for-index-underscore, merge-list-append, move-assign-in-block

import random
from Card import Card, Deck, Player

#Game Setup

Player1 = Player('Hardik')
Player2 = Player('Jay')

new_deck = Deck()
new_deck.shuffle()
#print(new_deck)


for x in range(26):
    Player1.add_cards(new_deck.deal_one())
    Player2.add_cards(new_deck.deal_one())

Game_ON = True

round = 0

while Game_ON:

    round = round + 1
    print(f'I am in round {round}')

    if len(Player1.all_cards) == 0:
        print('Player1 lost')
        Game_ON = False
        break

    if len(Player2.all_cards) == 0:
        print('Player2 lost')
        Game_ON = False
        break

    Player1_cards = []
    Player2_cards = []

    Player1_cards.append(Player1.remove_one())
    Player2_cards.append(Player2.remove_one())

    at_war = True

    while at_war:

        if Player1_cards[-1].value > Player2_cards[-1].value:
             Player1.add_cards(Player2_cards)
             Player1.add_cards(Player1_cards)
             at_war = False

        elif Player1_cards[-1].value < Player2_cards[-1].value:
             Player2.add_cards(Player2_cards)
             Player2.add_cards(Player1_cards)
             at_war = False

        else:
            print('WAR!')

            if len(Player1.all_cards) < 5:
                print('Player1 lost')
                Game_ON = False
                break

            elif len(Player2.all_cards) < 5:
                print('Player2 lost')
                Game_ON = False
                break

            else:
                for add_new_cards in range(5):
                    Player1.all_cards.append(Player1.remove_one())
                    Player2.all_cards.append(Player1.remove_one())