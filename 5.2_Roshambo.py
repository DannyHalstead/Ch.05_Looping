'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random

print("You are being forced to play rocket paper scissors for the rest of your life.")
UserChoice = int(input("Press 1 for Rock, Press 2 for Paper, Press 3 for Scissors."))
if UserChoice == 1:
    YourInterpret = "Rock"
elif UserChoice == 2:
    YourInterpret = "Paper"
else:
    YourInterpret = "Scissors"
print ("You choose", YourInterpret)

AIChoice = random.randint(1,3) #Get it because Ai don't have a choice haha pure comedy
if AIChoice == 1:
    Interpret = "Rock"
elif AIChoice == 2:
    Interpret = "Paper"
else:
    Interpret = "Scissors"
print ("The AI choose", Interpret)

if UserChoice == 3 and  AIChoice == 1: #Without this line you would win if you use scisors and the computer uses rock
    print("You lost.")
    LossCount += 1
else:
    if UserChoice +1 == AIChoice:
        print("You lost.")
        LossCount += 1
    elif UserChoice == AIChoice:
        print ("You tied.")
        TieCount += 1
    else:
        print("You won.")
        WinCount += 1