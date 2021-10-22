# a= input()
# b= input()
# c= input()
# d= input()
# if (( int(a) > 10 or int(b) > 10) or (int(c) > 10 or int(d) > 10)):
#     print("too high")
# elif (a==b and c==d):
#     print("correct")
# elif (a==b or b==c):
#     print("half")

"""this writes a program thats takes input from the user less than 10, and compares them, if
number is higher than 10 , it would trow an error"""

# grade = int(input())
# if (grade >= 70 and grade <=100):
#     print( "you got an A")
# elif (grade >= 60 and grade <= 70):
#     print( "you got a b")
# elif (grade >= 50 and grade <= 60):
#     print( "you got a c")
# elif (grade >= 40 and grade <= 50):
#     print( "you got a d")
# elif (grade >= 30 and grade <= 40):
#     print( "you got an e")
# elif (grade >= 0 and grade <= 30):
#     print( "you got an f")
# else:
#       print("you did not attend exam")

#this priject determins the grade of students in a test


#fizbutt challenge
# fizbutt=list(range(50))
# for i in fizbutt:
#     if i%2==0 :
#         continue
#     elif i%5==0 and i%3==0:
#         i="solo learn"x 
#         print(i)
#     elif i%3==0:
#         i="solo"
#         print(i)
#     elif i%5==0:
#         i="learn"
#         print(i) 
#     else:
#         print(i)

"""prints odd number from one one to 50
if number is a multiple of 5 and 3 , system prints solo learn
if number is a multiple of 3 , system prints solo
if number is a multiple of 5 , system prints learn"""

# password = input()
# retype = input()

# def validate(text1,text2 ):
#     if text1==text2:
#         print("welcome and you may proceed")
#     elif text1!= text2 :
#         print( "passwords do not match")

# validate(password, retype)

"""this code validates two passwords and see if they are both 
the same if they are differet , it would display an error."""

#differenciate
"""the following code prints the differenciated value of the 
passed figures"""
# def diff( x , y):
#     z=x*y
#     a =y-1
    
#     print(str(z)+ "*" +str(a))

# a=input()
# b=input()
# diff(a,b)

"""finding square root of numbers and cos of numbers and add them with import"""
# from math import sqrt, cos

# def surt(a):
#     s= cos(a)
#     t= sqrt(a)
#     u = s + t
#     print(u)

# g=int(input()) 
# surt(g)

"""celcius to fahrenheit calculator"""

def cal(x):
    a= 9/5
    val = a* x + 32
    print(val)

gh=int(input()) 
cal(gh)