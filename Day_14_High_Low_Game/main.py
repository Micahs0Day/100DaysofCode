from art import logo
from art import vs
from game_data import data
import random
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def high_low_game():
  print(logo)
  cont_game = True
  score = 0
  b = random.randint(0,len(data)-1)

  while cont_game == True:

    a = b
    b = random.randint(0,len(data)-1)
    if a == b:
      b = random.randint(0,len(data)-1)

    a_name = data[a]["name"]
    a_description = data[a]["description"]
    a_country = data[a]["country"]
    a_followers = data[a]["follower_count"]
    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")

    print(vs)
    
    b_name = data[b]["name"]
    b_description = data[b]["description"]
    b_country = data[b]["country"]
    b_followers = data[b]["follower_count"]

    print(f"Against B: {b_name}, a {b_description}, from {b_country}.")

    user_answer = input("\nWho has more followers? 'A' or 'B'? ").lower()

    if a_followers > b_followers and user_answer == "a" :
      score+=1
      clearConsole()
      print(logo) 
      print(f"You are correct! Current Score: {score}\n")
    elif b_followers > a_followers and user_answer == "b" :
      score+=1
      clearConsole() 
      print(logo)
      print(f"You are correct! Current Score: {score}\n")
    else:
      print(f"\nWrong, GAME OVER!!!, Final Score is {score}")
      cont_game = False 

high_low_game()
