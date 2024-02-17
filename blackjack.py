import random

dealer_deck = {
    1: ['Ace', 'Spades'], 
    2: ['2', 'Spades'], 
    3: ['3', 'Spades'], 
    4: ['4', 'Spades'], 
    5: ['5', 'Spades'], 
    6: ['6', 'Spades'], 
    7: ['7', 'Spades'], 
    8: ['8', 'Spades'], 
    9: ['9', 'Spades'], 
    10: ['10', 'Spades'], 
    11: ['Jack', 'Spades'], 
    12: ['Queen', 'Spades'], 
    13: ['King', 'Spades'],
    14: ['Ace', 'Hearts'], 
    15: ['2', 'Hearts'], 
    16: ['3', 'Hearts'], 
    17: ['4', 'Hearts'], 
    18: ['5', 'Hearts'], 
    19: ['6', 'Hearts'], 
    20: ['7', 'Hearts'], 
    21: ['8', 'Hearts'], 
    22: ['9', 'Hearts'], 
    23: ['10', 'Hearts'], 
    24: ['Jack', 'Hearts'], 
    25: ['Queen', 'Hearts'], 
    26: ['King', 'Hearts'],
    27: ['Ace', 'Clubs'], 
    28: ['2', 'Clubs'], 
    29: ['3', 'Clubs'], 
    30: ['4', 'Clubs'], 
    31: ['5', 'Clubs'], 
    32: ['6', 'Clubs'], 
    33: ['7', 'Clubs'], 
    34: ['8', 'Clubs'], 
    35: ['9', 'Clubs'], 
    36: ['10', 'Clubs'], 
    37: ['Jack', 'Clubs'], 
    38: ['Queen', 'Clubs'], 
    39: ['King', 'Clubs'],
    40: ['Ace', 'Diamonds'], 
    41: ['2', 'Diamonds'], 
    42: ['3', 'Diamonds'], 
    43: ['4', 'Diamonds'], 
    44: ['5', 'Diamonds'], 
    45: ['6', 'Diamonds'], 
    46: ['7', 'Diamonds'], 
    47: ['8', 'Diamonds'], 
    48: ['9', 'Diamonds'], 
    49: ['10', 'Diamonds'], 
    50: ['Jack', 'Diamonds'], 
    51: ['Queen', 'Diamonds'], 
    52: ['King', 'Diamonds']
}

def deal_card():
    card = random.randint(1, 52)
    connect = " of "
    str_deck = list(dealer_deck.get(card))
    print(('The ') + (connect.join(str_deck)))
    
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
    print('Your first card is...')
    deal_card()
    print('Your second card is...')
    deal_card()
    break
    