'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''

import random
YourFortniteMMR = 40
OtherPlayerMMR = 60
BadGrades = 0
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
        print("The other players MMR is", OtherPlayerMMR)
        print("You are this tired:", Tiredness)
        print("Your grades are this bad from one to ten ", BadGrades)
        print("Days until World cup:", DaysUntilWorldCup)
        continue
    elif TodaysChoice.upper() == "A":
        DaysUntilWorldCup -= 1
        Tiredness = 0
        print("You are now well rested.")
        OtherPlayerMMR += random.randint(7,14)
        print("The other players new MMR is", OtherPlayerMMR)
        print("Your Fortnite MMR and grades did not change.")
    elif TodaysChoice.upper() == "B":
        DaysUntilWorldCup -= 1
        YourFortniteMMR += random.randint(5,12)
        print("Your new MMR is", YourFortniteMMR)
        OtherPlayeMMR += random.randint(7, 14)
        print("The other players new MMR is", OtherPlayerMMR)
        Tiredness += 1
        BadGrades += 1
        "You are a bit more tired then before and your grades are a bit worse"
    elif TodaysChoice.upper() == "C":
        DaysUntilWorldCup -= 1
        YourFortniteMMR += random.randint(10, 20)
        print("Your new MMR is", YourFortniteMMR)
        OtherPlayeMMR += random.randint(7, 14)
        print("The other players new MMR is", OtherPlayerMMR)
        Tiredness += 1
        BadGrades += random.randint(1,3)
        print("You are a bit more tired then before and your grades are worse")
    elif TodaysChoice.upper() == "D":
        DaysUntilWorldCup -=1
        print("Your fortnite MMR did not change.")
        OtherPlayeMMR += random.randint(7, 14)
        print("The other players new MMR is", OtherPlayerMMR)
        print("You are the same amount of tired as yesterday")
        BadGrades = 0
        print("Your grades are good now.")

    if Tiredness > 6:
        print("You have died of tiredness.")
        break
    elif Tiredness > 4:
        print("You are very tired and need sleep soon.")
    if BadGrades >8:
        print("You failed out of school.")
        break
    elif BadGrades >5:
        print("You are doing really bad in school and need to study soon.")

    if DaysUntilWorldCup == 0:
        if YourFortniteMMR > OtherPlayerMMR:
            print ("You won")
            break
        else:
            print("You lost")
            break


print("Thanks for playing Fortnite pro simulator.")