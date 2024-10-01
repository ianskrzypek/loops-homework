#LOOPS CHALLENGES
#4. Alter the previous program to ask the user for a starting number and an 
#ending number. Display all the numbers in that range (including both the 
#starting and ending numbers they entered)

int41 = int(input("enter a starting number: "))
int42 = int(input("enter an ending number: "))
for i in range (int41,int42 + 1):
    print (int41)
    int41 = int41 + 1

#6) Ask the user to input a number and then ask if they want to double the 
#number. If they answer “y” multiply the number by 2 and display the answer.
#Keep repeating this loop, doubling their number each time, until they no 
#longer reply “y”

num6 = int(input("enter a number: "))
ans6 = input("would you like to double that number? (y for yes):")
while ans6 == ("y") or ans6 == ("yes"):
    num6 = num6*2
    print("your new number is: ",num6)
    ans6 = input("do want to double it again? (y for yes): ")


#WHILE LOOPS
#3)Ask the user to enter a number and then enter another number.  Add these two numbers together and then ask 
#if they want to add another number.  If they enter ‘y’, ask them to enter another number and keep adding
#numbers until they do not answer ‘y’.  Once the loop has stopped, display the total
ans3 = ("y")
num3t = int(input("enter a number: "))
while ans3 == ("y") or ans3 == ("yes"):
    num31 = int(input("enter another number: "))
    num3t = num31+num3t
    ans3 = input("do you want to add another number? (y for yes): ")
print ("the total of all your numbers is:",num3t)

#5) Create a variable called compnum and set the value to 50.  Ask the user to enter a number.  While their guess is 
#not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another
#guess.  If they enter the same value as compnum, display the message ‘Well done, you took [count] attempt
compnum5 = 50
guess5 = 1
try5 = 0
while guess5 != 50:
    guess5 = int(input("enter a number: "))
    try5 = try5 + 1
    if guess5 < 50:
        print ("too low, try again")
    elif guess5 > 50:
        print ("too high, try again")
print ("Well done, you took",try5,"attempts")

#FOR LOOPS
#5) Set a variable called total to 0.  Ask the user to enter five numbers and after each input ask them if they want 
#that number included. If they do, then add the number to the total.  If they do not want it included, don’t add it 
#to the total.  After they have entered all five numbers, display the total.

total5 = 0
for i in range (5):
    num5 = int(input("enter a number: "))
    inc5 = input("do you want to add your previous input to the total?(y for yes): ")
    if inc5 == ("y") or inc5 == ("yes"):
        total5 = total5 + num5
print ("your total is",total5)


#6) Ask which direction the user wants to count (up or down).  If they select up, then ask them for the top number 
#and then count from 1 to that number.  If they select down, ask them to enter a number below 20 and then 
#count down from 20 to that number.  If they entered something other than up or down, display the message ‘I 
#don’t understand.

up6 = input("enter a direction (only 'up' or 'down'): ")
if up6 == ("up"):
    top6 = int(input("enter a top number: "))
    for i in range (1,top6+1):
        print (i)
elif up6 == ("down"):
    lownum6 = int(input("enter a number under 20: "))
    for i in range (20,lownum6-1,-1):
        print (i)
else:
    print ("i don't understand")