# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
# Write all of your part 4 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
#
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
    # Implement card_name function here

    # Check if the card rank is valid
    if card_rank < 1 or card_rank > 13:
        print("BAD CARD")
        return
   
    # Dictionary to map card ranks to their names
    card_names = {
        1: "Ace",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        12: "Queen",
        13: "King"
    }
   
    # Get the card name from the dictionary
    name = card_names[card_rank]
   
    # Determine the correct article
    article = "an" if name in ["Ace", "8"] else "a"
   
    # Print the result
    print(f"Drew {article} {name}")

   

# Draws a new random card, prints its name, and returns its value.
#
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    # Implement draw_card function here

    card_rank =randint(1, 13)
    print_card_name(card_rank)
   
    if card_rank == 1:  # Ace
        return 11
    elif card_rank >= 11:  # Jack, Queen, King
        return 10
    else:
        return card_rank
# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
#
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
    # Implement print_header function here

    print("-----------")
    print(message)
    print("-----------")

# Prints turn header and draws a starting hand, which is two cards.
#
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
    # Implement draw_starting_hand function here
    print_header(f"{name} TURN")
    card1_value = draw_card()
    card2_value = draw_card()
       
    return card1_value + card2_value

# Prints the hand total and status at the end of a player's turn.
#
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    print(f"Final hand: {hand_value}.")
   
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.")

# Prints the end game banner and the winner based on the final hands.
#
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    print_header("GAME RESULT")
   
    if user_hand > 21:
        print("Dealer wins!")
    elif dealer_hand > 21 or user_hand > dealer_hand:
        print("You win!")
    elif user_hand < dealer_hand:
        print("Dealer wins!")
    else:
        print("Push.")
    # Implement print_end_game_status function here
#Fixed!Done.Correct!



# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail. 
from blackjack_helper import * 
 
# Write all of your part 4 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT. 
hand_value1=draw_starting_hand("YOUR") 
 
is_yes = True 
while hand_value1< 21 and is_yes: 
  should_hit = input('You have ' + str(hand_value1) + ". Hit (y/n)? ") 
  if should_hit == 'n': 
    is_yes = False 
  elif should_hit == 'y': 
        hand_value1=hand_value1+draw_card 
  else: 
    print("Sorry I didn't get that.") 
print_end_turn_status(hand_value1) 
hand_value=draw_starting_hand("DEALER") 
while hand_value < 17: 
        print(f"Dealer has {hand_value}.") 
        hand_value=hand_value+draw_card() 
print_end_turn_status(hand_value) 
print_end_game_status(hand_value1,hand_value) 
