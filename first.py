# print("samad")
# i = input()
# print ("my name is " + i) 
# i += " is a girl"
# print(i)
#  y = int(input())
#  y += "  is my age."
# print(y:= input())
# boolean
# print(3 == 9)
# print(3 != 9)
# print(3 > 9)
# print(3 >= 9)
# print(3 < 9)
# print(3 <= 9)
#if and else statements
# n = int(input())
# if n == 1:
#     print("one")
# elif (n==1 or n==2):
#     print ("one or two.") 
# else:
#  print("not allowed")
# print (1==1 and 2==2)
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
#multiple conditions


#lists
# words= ["hello", "world", "!"]
# empty_lists= []
# print(words[0])
# print(words[1])
# print(words[2])
"""string can also contain all types of variable types,
 for eiample:"""
# num = 23
# things= [ "words", 45, [ 2,"sat",num]]
# print (things[0])
# print (things[1])
# print (things[2][0])
# print (things[2][1])
# print (things[2][2])
"""string can also be indented like lists,
 eg:"""
# word= "hello world"
# print (word[0])
# print (word[1])
# print (word[2])
# print (word[3])
# print (word[4])
"""strings can also be reassigned , eg:"""
# num =[4,"red",4,4]
# num[3]= 5
# print(num[3])

"""append"""
# num=["samad"]
# # i= input()
"""#append alllows u to append any item to the end of a list """
# # num.append(i)
# index = 0
"""insert allow you to insert any item to any part of a list.
"""
# num.insert(index,"olalekan")
# num.insert(1,"Busari")
# print(num)
# print(len(num))
"""
while loop"""
# i =1
# while i < 10:
#     if i%2 == 0:
#         print(str(i) + " is even")
#     else:
#         print(str(i) + "is odd")
#     i += 1
# print("finish")

"""break is used to break a loop prematurely"""
# i = 0 
# while True:
#     print(i)
#     i += 1
#     if i >= 6:
#     #    print("breaking")
#        break
# print("finished")

"""continue statement""" 
# i=1
# while i<=5:
#     print(i)
#     i+=1
#     if i==3:
#         print('skipping 3')
#         continue

"""for loop"""
# words=["bread","egg","beans"]
# for item in words:
#     print(item + "!")


# string="samadmm"
# count=0
# for letters in string:
#     if (letters == 'a'):
#         count+=1

# print(count)
    
"""range
range prints numbers from 0 to the the specified numeber
to output its contents , it must first be converted to a list
using the list() function"""
# numbers= list(range(20))
# print(numbers[6])

"""the range of a list can also be specified, from initial to final.
"""# numbers= list(range(3,8))
# print(numbers)

#they are both the same
# print(range(20) == range(0,20))

"""the first  variable represent the initial number
"""#the second is the ending 
#the third is the multiples of the range
# numbers= list(range(5,20,4))
# print(numbers)

# students= ["samad", "emanuel", "bolu", "oche"]
# for stu in range(0,len(students)):
#     if stu == 4:
#         break
#     else:
#         print(students[stu])

#         print("counter is "+ str(stu))

# print("program complete")

"""functions
funcions are decleared with the keywork DEF"""
#For example:
#this line would declear the function
# def hello():
#     print("hello world")

"""this line would print the function"""
# hello()

"""some function also take in arguments , for example:"""
# def emanuel(age, likes):
#     print( "emanuel is " + str(age) + "years old and he likes " + likes)

# emanuel(23, "games")

"""return key work"""
# def max(x, y):
#     if x>= y:
#         return x
#     else :
#         return y

# print(max(4,6))
#
#
"""functions can also be varibles of other functions , for example:"""
# def add(x,y):
#     return x + y

# def do_twice(func,x,y):
#     return func(func(x,y),func(x,y))

# a= 4
# b=  5
# print(do_twice(add , a , b))

"""modules"""
"""piece of code written by other people for a specified task"""
import random
"""random helped print 5 random numbers from the random key"""
for i in range(5):
    value = random.randint(1,4)
    print(i)

