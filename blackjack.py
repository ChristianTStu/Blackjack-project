import random

dealer_deck = [
    ['Ace', 'Spades'], 
    ['2', 'Spades'], 
    ['3', 'Spades'], 
    ['4', 'Spades'], 
    ['5', 'Spades'], 
    ['6', 'Spades'], 
    ['7', 'Spades'], 
    ['8', 'Spades'], 
    ['9', 'Spades'], 
    ['10', 'Spades'], 
    ['Jack', 'Spades'], 
    ['Queen', 'Spades'], 
    ['King', 'Spades'],
    ['Ace', 'Hearts'],  
    ['2', 'Hearts'], 
    ['3', 'Hearts'], 
    ['4', 'Hearts'], 
    ['5', 'Hearts'], 
    ['6', 'Hearts'], 
    ['7', 'Hearts'], 
    ['8', 'Hearts'], 
    ['9', 'Hearts'], 
    ['10', 'Hearts'], 
    ['Jack', 'Hearts'], 
    ['Queen', 'Hearts'], 
    ['King', 'Hearts'],
    ['Ace', 'Clubs'],
    ['2', 'Clubs'], 
    ['3', 'Clubs'],
    ['4', 'Clubs'], 
    ['5', 'Clubs'], 
    ['6', 'Clubs'], 
    ['7', 'Clubs'], 
    ['8', 'Clubs'],
    ['9', 'Clubs'], 
    ['10', 'Clubs'], 
    ['Jack', 'Clubs'],
    ['Queen', 'Clubs'], 
    ['King', 'Clubs'],
    ['Ace', 'Diamonds'], 
    ['2', 'Diamonds'], 
    ['3', 'Diamonds'], 
    ['4', 'Diamonds'], 
    ['5', 'Diamonds'],
    ['6', 'Diamonds'], 
    ['7', 'Diamonds'], 
    ['8', 'Diamonds'], 
    ['9', 'Diamonds'], 
    ['10', 'Diamonds'], 
    ['Jack', 'Diamonds'], 
    ['Queen', 'Diamonds'], 
    ['King', 'Diamonds']
]

used_cards = [

]

def burn_card():
    rand_card = random.randint(0, 51)
    burn_card = dealer_deck.pop(rand_card)
    used_cards.append(burn_card)

def deal_card():
    rand_card = random.randint(0, len(dealer_deck))
    connect = " of "
    str_deck = dealer_deck[rand_card]
    remove_card = dealer_deck.pop(rand_card)
    used_cards.append(remove_card)
    print('Your first card is...')
    print(('The ') + (connect.join(str_deck)))

def deal_2nd_card():
    rand_card = random.randint(0, len(dealer_deck))
    connect = " of "
    str_deck = dealer_deck[rand_card]
    remove_card = dealer_deck.pop(rand_card)
    used_cards.append(remove_card)
    print('Your second card is...')
    print(('The ') + (connect.join(str_deck)))

def deal_card_dealer():
    rand_card = random.randint(0, len(dealer_deck))
    remove_card = dealer_deck.pop(rand_card)
    used_cards.append(remove_card)
    print("The dealer's first card is hidden.")

def deal_2nd_card_dealer():
    rand_card = random.randint(0, len(dealer_deck))
    connect = " of "
    str_deck = dealer_deck[rand_card]
    remove_card = dealer_deck.pop(rand_card)
    used_cards.append(remove_card)
    print("The dealer's second card is...")
    print(('The ') + (connect.join(str_deck)))


def round_deal_phase():
    deal_card()
    deal_card_dealer()
    deal_2nd_card()
    deal_2nd_card_dealer()

    
# Introduction

print('Welcome to the House of Blackjack. Where we always win!')
play_response = input('Would you like to play? Yes or No:')

if play_response.lower =='':
    print('No input provided, please restart the program.')

    exit()

elif play_response.lower() =='yes':
    pass

elif play_response.lower() =='no':
    print('Well okay! Please restart the program if you would like to use me later!')

    exit()

else:
    print('Not a vaild response, please restart the program.')

    exit()

# Game Loop
    
while play_response.lower() =='yes':
    round_deal_phase()
    break