import random

n= int(input("enter range:"))
score=0
a=0

while(a<3):
  userInput = int(input("Enter your number:--"))
  while(userInput<n):
    a+=1
    Cnumber = random.randrange(1,n)
    if (userInput > Cnumber):
         print("Computer Number: ", Cnumber)
         print("Have one more try. Your Guess Number was too high")
         break
    elif (Cnumber > userInput):
        print("Computer Number: ", Cnumber)
        print("Have one more try. Your Guess Number was too low")
        break
    else:
        print("Computer Number", Cnumber)
        print("Your Guess Number is equal") 
    if(userInput == Cnumber):
      score+=1
print("Your score is:",score)

if(score>0):
  print("Congrat's")
else:
  print("Better Luck Next Time!")