  #Sign your name: DannyH

'''
 1. Make the following program work.
   '''  

print("This program takes three numbers and returns the sum.")
Total = 0
for i in range(3):
    NumberBeingAdded = float(input("Enter a number: "))
    Total += NumberBeingAdded
print("The total is:",Total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even.              
     numbers from 2 to 100, inclusive.
'''
print('Watch in amazement as the odd numbers from 2-100 are printed.')
for i in range (2,101,2):
    print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

NumbersLeft = 10
while NumbersLeft >= 0:
    print(NumbersLeft)
    NumbersLeft -= 1
print("Blastoff!")




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).                    
'''

import random
random=random.randint(1,10)
print("Your random number is:", random)




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''

total = 0
PositiveCount = 0
NegetiveCount =0
ZeroCount = 0
print("You are going to enter seven numbers")

for i in range (7):
    userinput=float(input("Number to enter."))
    if userinput > 1:
        PositiveCount += 1
    elif userinput < 1:
        NegetiveCount += 1
    elif userinput == -0:
        print("Why would you even enter -0?")             #I just wanted to make an easter egg ok but Python dosn't understand when you type -0   :(
        ZeroCount += 1
    else:
        ZeroCount +=1

    total += userinput
print("The total of your numbers is:", total)
print("You had this many positive numbers:", PositiveCount)
print("You had this many negetive numbers:", NegetiveCount)
print("You had this many zeros:", ZeroCount)