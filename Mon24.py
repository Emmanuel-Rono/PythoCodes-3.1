
#ALERT
#Assignment to calculate pay==fROM(LINE 57-67)


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






