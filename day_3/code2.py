# fruits = [ "apple", "banana","Guava"]

# for fruit in fruits :
#     print(fruit)


# ------------------------------------------------------------


# count = 1

# while count <=5:
#     print(count)
#     count += 1


# -----------------------------------------------

# numbers = [ 1,2,3,4,5,6]

# for number in numbers:
#     if number % 2==0:
#         print(f"{number} is even")
#     else :
#         print(f"{number} is odd")    



#  Assignment 

# get user input 
number = int(input("enter a number : "))

# check if the no is positive , negative or zero 

if number > 0 :
    print(f"{number} is positive")
elif number <0 :
    print(f"{number} is negative") 
else :
    print(" it is zero")  

# print numbers from 1 to input 

num =0
while num < number :
    print(num)
    num+=1
    