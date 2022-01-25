#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

rock = []
paper = []
scissors = []
x = input("Enter rock, paper, or scissors")

def choice(x):
 print("rock : 0\npaper : 1\nscissors : 2")
 if x == "rock":
   return 0
 if x == "paper":
   return 1
 if x == "scissors":
   return 2

g = choice(x)

"""
def playerChoice():
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  return value


if __name__ == "__main__":
  player = playerChoice()
  print(player)
"""