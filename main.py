rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

def rps(u, c):
  
  if u == c:
    return ("\nIt's a tie!\n")
        
  elif (u == 'r' and c == 's'):
    print(f"\n{name}: \n", rock)
    print("\nBot: \n", scissors)
    return "\nYou Win!"

  elif (u == 'p' and c == 'r'):
    print(f"\n{name}: \n", paper)
    print("\nBot: \n", rock)
    return "\nYou win!"
    
  elif (u == 's' and c == 'p'):
    print(f"\n{name}: \n", scissors)
    print("\nBot: \n", paper)
    return "\nYou win!"
      
  else:
    if (c == 'r' and u == 's'):
      print("\nBot: \n", rock)
      print(f"\n{name}: \n", scissors)
      return "\nYou lose!"
      
    elif (c == 'p' and u == 'r'):
      print("\nBot: \n", paper)
      print(f"\n{name}: \n", rock)
      return "\nYou lose!"
    
    elif (c == 's' and u == 'p'):
      print("\nBot: \n", scissors)
      print(f"\n{name}: \n", paper)
      return "\nYou lose!"

    else:
      print("Invalid input!")
      return "Game exited automatically..."


name = str(input("\nEnter your good name here: "))
print(f"\nWhat's your choice {name}?")
x = str(input("\nChoose 'r' 4 rock, 'p' 4 paper, 's' for scissors: "))
y = random.choice(['r','s', 'p'])

print(f"\n{name} choose {x} and, Bot Choose {y}")
print(rps(x, y))