'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''

FortniteMMR = 0
Tiredness = 0
FailingSchool = 0

Done = False
print ("Welcome to Fortnite pro simulator. In this game your goal is to qalify for the Fortnite world cup without failing school or dying from lack of sleep.")
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
    if TodaysChoice.upper() == "F":
        pass
    if TodaysChoice.upper() == "A":
        pass
    elif TodaysChoice.upper() == "B":
        pass
    elif TodaysChoice.upper() == "C":
        pass
    elif TodaysChoice.upper() == "D":
        pass


print("Thanks for playing Fortnite pro simulator!")