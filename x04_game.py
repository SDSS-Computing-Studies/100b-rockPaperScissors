#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

while True:
 rock = []
 paper = []
 scissors = []
 x = input("Enter rock, paper, or scissors")

 def choice(x):
  if x == "rock":
    return 0
  if x == "paper":
    return 1
  if x == "scissors":
    return 2

 g = choice(x)

 t = []
 def random(t):
  import random
  mylist = [0, 1, 2]
  return random.choice(mylist)

 k = random(t)

 def funchoice(k,g):
   if k == g:
     return(0)
   elif g == 0:
         if k == 1:
             return(-1)
         else:
           return(1)
   elif g == 1:
         if k == 2:
             return(-1)
         else:
             return(1)
   elif g == 2:
         if k == 0:
             return(-1)
         else:
             return(1)

 j = funchoice(k,g)
 print(j)

"""
from x01_player import *
from x02_computer import *
from x03_winner import *

if __name__ == "__main__":
  pass
"""
