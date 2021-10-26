#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random 
import os
from logo import logo

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def keepplaying():
  playagain = input("\nPlay again? 'Y' or 'N' ").lower()
  if playagain == "y":
    clearConsole()
    return number_checker()
  if playagain == "n":
    clearConsole()
    return 

def guesschecker(comp_guess, user_guess, counter):
  while counter == 0:
    if user_guess < comp_guess:
      print("Too Low.")
    elif user_guess > comp_guess:
      print("Too High.")

    print("\nGame Over...")
    print(f"The answer was {comp_guess}")
    keepplaying()
    return False
  if user_guess < comp_guess:
    print("Too Low.")
    print("Guess again.\n")
    return False
  elif user_guess > comp_guess:
    print("Too High.")
    print("Guess again.\n")
    return False
  elif user_guess == comp_guess:
    return True
  
def number_checker():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  random_number = random.randint(0,100)
  game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if game_mode == "easy":
    print(f"Pssst, the correct answer is {random_number}")
    i = 10
    while i != 0: 
      print(f"You have {i} attempts left to guess the number...")
      guess = int(input("Guess the number: "))
      i -= 1
      if guesschecker(random_number, guess, i) == True:
        print(f"You got it! The answer was {random_number}")
        i = 0
        keepplaying()
  elif game_mode == "hard":
    print(f"Pssst, the correct answer is {random_number}")
    i = 5
    while i != 0:
      print(f"You have {i} attempts left to guess the number...")
      guess = int(input("Guess the number: "))
      i -= 1
      if guesschecker(random_number, guess, i) == True:
        print(f"You got it! The answer was {random_number}")
        i = 0
        keepplaying()
  else:
    print("Enter a valid game mode...")
    return number_checker()



number_checker()