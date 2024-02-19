def main():
    print('Welcome to the House of Blackjack. Where we always win!')

import random

suits = [
    'Hearts',
    'Diamonds',
    'Spades',
    'Clubs'
]

cards_in_deck = [
    'Ace',
    '2',
    '3', 
    '4',
    '5',
    '6',  
    '7', 
    '8', 
    '9', 
    '10',
    'Jack',
    'Queen',
    'King'
]

player_cards = [

]

dealer_cards = [

]

aces = [
    'Ace of Spades', 
    'Ace of Hearts',
    'Ace of Clubs',
    'Ace of Diamonds'
]

twos= [
    '2 of Spades', 
    '2 of Hearts',
    '2 of Clubs',
    '2 of Diamonds'

]

threes = [
    '3 of Spades', 
    '3 of Hearts',
    '3 of Clubs',
    '3 of Diamonds'
]

fours = [
    '4 of Spades', 
    '4 of Hearts',
    '4 of Clubs',
    '4 of Diamonds'
]

fives = [
    '5 of Spades', 
    '5 of Hearts',
    '5 of Clubs',
    '5 of Diamonds'
]

sixes= [
    '6 of Spades', 
    '6 of Hearts',
    '6 of Clubs',
    '6 of Diamonds'
]
sevens = [
    '7 of Spades', 
    '7 of Hearts',
    '7 of Clubs',
    '7 of Diamonds'
]
eights = [
    '8 of Spades', 
    '8 of Hearts',
    '8 of Clubs',
    '8 of Diamonds'

]
nines = [
    '9 of Spades', 
    '9 of Hearts',
    '9 of Clubs',
    '9 of Diamonds'
]
tens = [
    '10 of Spades', 
    '10 of Hearts',
    '10 of Clubs',
    '10 of Diamonds',
    'Jack of Spades',
    'Jack of Hearts',
    'Jack of Clubs',
    'Jack of Diamonds',
    'Queen of Spades',
    'Queen of Hearts',
    'Queen of Clubs',
    'Queen of Diamonds', 
    'King of Spades',
    'King of Hearts',
    'King of Clubs',
    'King of Diamonds'

]


def deal_card():
    rand_suit = random.randint(0, (len(suits) - 1))
    rand_num = random.randint(0, (len(cards_in_deck) - 1))
    rand_card = cards_in_deck[rand_num] + ' of ' + suits[rand_suit]
    if rand_card in player_cards:
        deal_card()
    elif rand_card in dealer_cards:
        deal_card()
    else:
        player_cards.append(rand_card)
        return rand_card
    
def deal_card_dealer():
    rand_suit = random.randint(0, (len(suits) - 1))
    rand_num = random.randint(0, (len(cards_in_deck) - 1))
    rand_card = cards_in_deck[rand_num] + ' of ' + suits[rand_suit]
    if rand_card in player_cards:
        deal_card_dealer()
    elif rand_card in dealer_cards:
        deal_card_dealer()
    else:
        dealer_cards.append(rand_card)
        return rand_card
    
def player_hand_check():
    hard_count = 0
    ace_check = 0
    for card in player_cards:
        if card in aces:
            hard_count += 1
            ace_check += 11
        elif card in twos:
            hard_count += 2
        elif card in threes:
            hard_count += 3
        elif card in fours:
            hard_count += 4
        elif card in fives:
            hard_count += 5
        elif card in sixes:
            hard_count += 6
        elif card in sevens:
            hard_count += 7
        elif card in eights:
            hard_count += 8
        elif card in nines:
            hard_count += 9
        elif card in tens:
            hard_count += 10

    soft_count = (hard_count - 1) + ace_check

    if soft_count == 21:
        print(f'Winner Winner, Chicken Dinner. Thats 21. Blackjack!!!')
    elif soft_count > 21:
        print(f'You have two Aces!! Wow :). That makes your hard count 22, becasue fo this you must choose your soft count of: {soft_count}. How would you like to proceed?')
    elif soft_count > 0 and soft_count < 21:
        print(f' You have an Ace! Your hard count is: {hard_count}. Your soft count of: {soft_count}. How would you like to proceed?')
    else:
        print(f'Your hard total is: {hard_count}.')
        

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
    
# Main Game Loop
while True:
    print('Your first card is...')
    print(deal_card())
    deal_card_dealer()
    print("The dealer's first card is hidden.")
    print('Your second card is...')
    print(deal_card())
    print("The dealer's second card is...")
    print(deal_card_dealer())
    player_hand_check()
    break