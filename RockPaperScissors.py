# RockPaperScissors.py
# December Redinger
# 3/15/2020

'''

This game of Rock, Paper, Scissors could be used in different programs as a sort of random decider. Many systems use "Paper beats Rock, Rock beats Scissors, Scissors beat Paper", 
and this sort of function could be used in many different ways. That's the hope, anyway.

'''


# Input: Player choice, then opponent choice.
# Process: Conflict evaluation and resolution.
# Output: Outcome is shown.


from random import randint
import sys


# List to pull random decisions from.

deciderList = ['Rock', 'Paper', 'Scissors']


def decider():

    decision = deciderList[randint(0, 2)]
    return str(decision)


def main():
    # Input: Player choice.

    choice = input(("Rock, Paper, or Scissors? (Capitalize first letter. "))

    # Opponent choice.

    opp_choice = decider()
    # Process: if/then branches for loss/win.

    if choice == 'Rock' and opp_choice == 'Paper':
        playerLoss = True
    elif choice == 'Paper' and opp_choice == 'Scissors':
        playerLoss = True
    elif choice == 'Scissors' and 'opp_choice' == 'Rock':
        playerLoss = True
    elif choice == opp_choice:
        print("Your choice was", choice, ". Your opponents choice was",
              opp_choice, ". You tied! Play again!")
        sys.exit
    else:
        playerLoss = False

    # Output: Outcome is shown!

    print("Your choice was", choice,
          ". Your opponents choice was ", opp_choice, )
    if playerLoss == True:
        print(opp_choice, "defeats", choice,
              ". Everyone loses sometimes. Please play again!")
    else:
        print(choice, "defeats", opp_choice,
              ". Congratulations! Please play again!")


main()
