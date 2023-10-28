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

#Write your code below this line 👇
import random 
print("Welcome: To Rock paper and scissors Game:)\n")
print("type 0 for rock, 1 for paper, 2 for scissors\n")
user=int(input("enter your choice\n"))
comp=random.randint(0,2)
if user==0 and comp==0:
  print("you choose rock\n")
  print(rock)
  print("computer also chooses rock\n")
  print(rock)
  print("its a tie")
elif user==0 and comp==1:
  print("you choose rock\n")
  print(rock)
  print("computer chooses paper\n")
  print(paper)
  print("you lose")
elif user==0 and comp==2:  
  print("you choose rock\n")
  print(rock)
  print("computer chooses scissors\n")
  print(scissors)
  print("you win")
elif user==1 and comp==0:
  print("you choose paper\n")
  print(paper)
  print("computer chooses rock\n")
  print(rock)
  print("you win")
elif user==1 and comp==1:
  print("you choose paper\n")
  print(paper)
  print("computer chooses paper\n")
  print(paper)
  print("its a tie")
elif user==1 and comp==2:
  print("you choose paper\n")
  print(paper)
  print("computer chooses scissors\n")
  print(scissors)
  print("you lose")
elif user==2 and comp==0:
  print("you choose scissors\n")
  print(scissors)
  print("computer chooses rock\n")
  print(rock)
  print("you lose")
elif user==2 and comp==1:
  print("you choose scissors\n")
  print(scissors)
  print("computer chooses paper\n")
  print(paper)
  print("you win")
elif user==2 and comp==2:
  print("you choose scissors\n")
  print(scissors)
  print("computer chooses scissors\n")
  print(scissors)
  print("its a tie")
