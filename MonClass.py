
#ALERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Assignment to calculate pay==fROM(LINE 57-67)
#,Monday 7/02/2022-from line 140-231
#*****************************************
#Python class notes and learning 
#:Richard Mathenge



#operators
from math import remainder
from platform import python_branch


c="Ëmmanuel Rono"
a=100
b=51
#add
sum=a+b
#subbtrat=ct
subtract=a-b
#times
times=a*b
#division
division=a/b
#power
power=a**b

#remainder
remainder=a%b
#to print
print("sum=",sum)
print("subtract=",subtract)
print("times=",times)
print("division=",division)
print("power=",power)
print("remainder",remainder)
#To check the datatype
"""To print the datatype"""
print(type(a),(b))
print(type(c))
"""Type conversion"""
#to convert to int
""" python concatination"""
a="hello "
b="python"
c=(10) #initialized to string
print(a+b) #print hello python

#print(a+c) return an error bcoz a=int and c=string
"""Solution is to convert c to string"""
c=str(10)#Conversioon to string ..
print(a+c)
print(type(c)) #check type of c

"""Assignment to calculate pay"""

import time      #to sleep for defined time
a=int(input("Enter Hours:"))#Convert to int
b=float(input("Enter Rate"))#convert to float
pay=a*b                    #calculate the pay
print("Pay=",pay)          #Return the pay

print("Exiting in 1 minute.......")  #alert
time_duration = 60  #duration
time.sleep(time_duration)#access the duration

#MONDAY 31/01/2022
#operators class
#write a  program to check wheter a numberis even
number=int(input("Enter a number:"))
if (number % 2==0):
        print("even")
else:
    print("Odd")



#program to check wheter a number is divisible by 5
number=int(input("Enter a number to check:"))
if(number%5==0):
     print("dividible")
     else:
         print("Indivisible")
         num=int(input("Value:"))

         #Program to check wheter it is divisible by 7
rem=int(num%2) #Decleared rem value
if(rem == 0): #If statement 
    print("Done...")
else:
    print("Not!!!!!!")


    #Automating the process of checking the if a value is divisible by 
    num=int(input("Value:"))
val=int(input("Enter Divisor to check: "))
rem=int(num%val ) #Decleared rem value
if(rem == 0): #If statement 
    print("Done...")
else:
    print("Not!!!!!!")

#Relational operator
a=10
b=5
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
#Program to calculate if to give discount
import  time
amount=int(input("Enter amount:"))
discount=0.05*amount #Amount discount
if(amount>5000):
    print("5% discount given")
    print("Discount:", discount)
else:
    print("There is no discount")
    print("Exiting in 10 minute...")
time_duration = 20  #duration
time.sleep(time_duration)#access the duration

#Code to check the tallest amoung 3 students
john=170
Alice=172
Bob=150
if(john>Alice and Bob):
    print("john is 170cm:")
elif(Alice>john and Bob):
    print("Alice is 172 cm:")
elif(Bob>Alice and john):
    print("Bob is 150cm")
else:
        print("Alice is tall")

        #Monday 07 /02/2022
a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
c=int(input("Enter third Number:"))
if a>b and a>c:
    print("A is greatest")
    # TODO: write code...
if b>a and b > c:
     print ("B us greater")
if c > a and c > b:
     print("B is greater")
     

#py program to check determine the amount of bonus to be given
import time 
salary=int(input("Your salary:"))
exp=int(input("Enter period:"))
if(exp>10):
  
     bonus = 0.01*salary
     print("bonus 10%=",salary)
  
if  exp>=6 and exp<=10:
    
     bonus= 0.8*salary
     print("bonus 8%=", salary)
    
elif(exp<6):
    
    bonus= 0.5*salary
    print("bonus 5% =", salary)
    print("Exiting in 20 seconds...")
time_duration = 20  #duration
time.sleep(time_duration)#access the duration

    


 
score=int (input("score1:"))
if (score<0 or score >100):
    print("Errror , score cannot exceed 100, and < 0")
    exit(0)
score=int (input("score2:"))
if (score<0 and score >100):
    print("Errror , score cannot exceed 100, and < 0")
    exit(0)
score=int (input("score3:"))
if (score<0 and score >100):
    print("Errror , score cannot exceed 100, and < 0")
    exit(0)
score=int (input("score4:"))
if (score<0 and score >100):
    print("Errror , score cannot exceed 100, and < 0")
    exit(0)
score=int (input("score5:"))
if (score<0 and score >100):
    print("Errror , score cannot exceed 100, and < 0")
    exit(0)
sum=score+score+score+score+score
average=sum/5
#if (score<0 and score >100):
    #print("Errror , score cannot exceed 100, and < 0")
if (average>=70 and average <=100):
    print("Grade","A")
    # TODO: write code...
elif(average>=60 and average <=69):
    print("Grade","B")
    # TODO: write code...
elif (average>=50 and average <=59):
    print("Grade",C)
    # TODO: write code...
elif (average>=40 and average <=49):
    print("Grade","D")
    # TODO: write code...
elif(average>=0 and average <=39):
    print("Grade","FAIL dude....")
    # TODO: write code...
elif(average<0 and average >100):
    print("Error, average should be within 0-100")
    

    #if statement to check the various if functionability
    nationality=["kenya,india"]
nationaliti=(input("nationality:"))
age=int(input("Age:"))
if (nationaliti in nationality ==kenya):
 if(age>=18):
   print("Eligible")
  print("18years")
 print("kenya")
    # TODO: write code...



    