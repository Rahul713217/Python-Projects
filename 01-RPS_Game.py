# Rock,Paper,Scissors Game
print("For Rock type 'r', for Paper type 'p' and for Scissors type 's' ")
print(" **** you type wrong, you lose due to invaild input")
import random
r = random.randint(1,3)
if r == 1:
    c = 'r'
elif r == 2:
    c = 'p'
else:
    c = 's' 

y = input('Rock(r), Paper(p) or Scissors(s) ? ')

if c == y:
    print("Draw")
elif (c == 'r' and y == 'p') or (c == 'p' and y == 's') or (c == 's' and y == 'r'):
    print("*********  You Win  *********")
else:
    print("!!!!!!!!!!!  You Lose  !!!!!!!!!!!")

print(f"Computer choose {c}")
