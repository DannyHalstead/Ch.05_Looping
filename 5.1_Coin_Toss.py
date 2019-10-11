'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

import random
Headcount = 0
Tailcount = 0
for i in range(50):
    currentflip = random.randint(0, 1)
    if currentflip == 0:
        Headcount += 1
        print("Heads")
    else:
        Tailcount += 1
        print("Tails")
print("Out of 50 flips, you got heads", Headcount, "times and you got tails", Tailcount, "times.")