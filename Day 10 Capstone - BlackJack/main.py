from art import logo
import random
import os

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_dealer_hand():
  hand = [0,0]
  for card in range(0,len(hand)):
    hand[card] = random.choice(cards)
  if sum(hand) > 21:
    for i in range(0, len(hand)):
      if hand[i] == 11:
          hand[i] = 1
      return hand
  else:
    return hand

def get_player_hand():
  hand = [0,0]
  for card in range(0,len(hand)):
    hand[card] = random.choice(cards)
  if sum(hand) > 21:
    for i in range(0, len(hand)):
      if hand[i] == 11:
          hand[i] = 1
      return hand
  else:
    return hand

def hit_deck(hand):
  x = random.randint(0,len(cards)-1)
  new_card = [0]
  new_card[0] = cards[x]
  new_hand = hand + new_card
  return new_hand

def get_current_score(hand):
  total = sum(hand)
  return total

def blackjack(): 
  cont_game = True
  while cont_game is True:
    answer = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower()
    if answer == "n":
      return
    clearConsole() 
    print(logo)
    player_hand = get_player_hand()
    dealer_hand = get_dealer_hand()

    player_score = get_current_score(player_hand)
    dealer_score = get_current_score(dealer_hand) 

    print(f"Your cards: {player_hand}, Current score: {player_score}")
    print(f"Dealers hand: [{dealer_hand[0]}, ?]")

    if player_score == 21:
      print("Player Wins!!!")
      return blackjack()
    elif dealer_score == 21:
      print(f"*Dealer reveals hand*: {dealer_hand}, 21!!!")
      print("Dealer Wins!!!")
      return blackjack()
    elif dealer_score == 21 and player_score == 21:
      print("It's a Draw!")
      return blackjack()
    else:
      answer = input("Type 'Y' to get another card, type 'N' to pass: ").lower()

    while answer == "y" and player_score <= 21:
      player_hand = hit_deck(player_hand)
      player_score = get_current_score(player_hand)
      print(f"\nYour cards: {player_hand}")
      print(f"Player's current score: {player_score}") 
      if player_score > 21 :
        if(11 in player_hand):
          ace = player_hand.index(11)
          player_hand[ace] = 1
          player_score = get_current_score(player_hand) 
          print(f"\nYou went over, Ace turns into 1: {player_hand}")
          print(f"Player's current score: {player_score}") 
          answer = input("\nType 'Y' to get another card, type 'N' to pass: ").lower()
        else:
          print("\nPlayer went over...")
          print("Dealer Wins!!!\n")
          return blackjack()
      elif player_score == 21:
        print("Player Wins!!!\n")
        return blackjack()
      else:
        answer = input("Type 'Y' to get another card, type 'N' to pass: ").lower()
  
    while answer == "y" and player_score > 21:
      print("Dealer Wins!!!\n")
      return blackjack()

    while answer == "n":
      print(f"\nDealer's hand: {dealer_hand}")   
      print(f"Dealer Score: {dealer_score}")
      while dealer_score <= player_score:
        if dealer_score < 21 or dealer_score <= player_score:
          dealer_hand = hit_deck(dealer_hand)
          print(f"\nDealer Hits: {dealer_hand}")
          player_score = get_current_score(player_hand)
          dealer_score = get_current_score(dealer_hand) 
          print(f"Dealer has: {dealer_score}")
          print(f"Player has: {player_score}")        
      if dealer_score > player_score and dealer_score <= 21:       
          print("\nDealer Wins!!!\n")
          return blackjack()
      elif player_score > dealer_score:
          print(f"\nDealer's hand: {dealer_hand}")
          print(f"Dealer Score: {dealer_score}")   
          print("Player Wins!!!\n")
          return blackjack()
      elif dealer_score > 21:
          if(11 in dealer_hand):
            ace2 = dealer_hand.index(11)
            dealer_hand[ace2] = 1
            dealer_score = get_current_score(dealer_hand) 
            print("\nDealer went over, Ace turns into 1...")
          else:
            print("\nDealer went over...")
            print("Player Wins!!!\n")
            return blackjack()


blackjack()

