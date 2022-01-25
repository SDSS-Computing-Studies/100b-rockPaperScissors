#!python3

"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""
t = []
def random(t):
 import random
 mylist = [0, 1, 2]
 return random.choice(mylist)

k = random(t)


"""
def computerChoice():
  
  return value

if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
"""

