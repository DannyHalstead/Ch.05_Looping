'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''

import random
YourFortniteMMR = 40
OtherPlayeMMR = 60
Grades = 100
Tiredness = 0
DaysUntilWorldCup = 30

Done = False
print ("Welcome to Fortnite pro simulator. In this game your goal is to qalify for the Fortnite world cup without failing school or dying from lack of sleep.")
print("To qualify, in 30 days you must have more MMR than the other players.")
while not Done:

    print("A to sleep today.")
    print("B to grind fortnite for 4 hours today.")
    print("C to grind Fortnite for 10 hours today")
    print("D to study today.")
    print("F to see your current status. (This will NOT use up todays action)")
    print("G to give up on your goal of becoming a pro Fortnite player, exits game.")

    TodaysChoice = str(input("What are you going to do today? "))
    if TodaysChoice.upper() == "G":
        break
        Done = True
    elif TodaysChoice.upper() == "F":
        print("Your MMR is", YourFortniteMMR)
        print("The other players MMR is", OtherPlayeMMR)
        print("You are this tired:", Tiredness)
        print("Your grades are", Grades)
        print("Days until World cup:", DaysUntilWorldCup)
        continue
    elif TodaysChoice.upper() == "A":
        DaysUntilWorldCup =- 1
        Tiredness = 0
        print("You are now well rested.")
        MMROthersGainedToday = random.randint(7,14)
        OtherPlayeMMR += MMROthersGainedToday
        Print("The other players new MMr is:", OtherPlayeMMR)
        print("Your Fortnite MMR and grades did not change.")
    elif TodaysChoice.upper() == "B":
        pass
    elif TodaysChoice.upper() == "C":
        pass
    elif TodaysChoice.upper() == "D":
        pass


print("Thanks for playing Fortnite pro simulator!")