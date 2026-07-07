# Python Fundamentals
# (Assignment1)
# Assignment Problems


# Q1. Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%


#  salary=int(input("Enter your salary: "))
# if salary < 30000:
#     final_salary=salary-((salary*5)/100)
#     print("tax on this salary is 5%")
#     print("After tax your salry :",final_salary)
# elif salary >= 30000 and salary < 70000:
#     final_salary=salary-((salary*15)/100)
#     print("tax on this salary is 15%")
#     print("After tax your salry :",final_salary)
# else:
#     final_salary=salary-((salary*25)/100)
#     print("tax on this salary is 25%")
#     print("After tax your salry :",final_salary)



# Q2. Write a function that takes two integers and and prints all even numbers between them (inclusive).


# num1=int(input("Enter First number: "))
# num2=int(input("Enter Second number: "))
# print("the even numbers between ",num1," and ",num2," : ")
# for i in range(num1,num2,):
#     if i%2==0:
#         print(i)



# Q3. Write a function that prints the digits of a number, n .
# For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [Hint - The right most digit of a number N is N%10.
# And to remove the right most digit from a number, we can do N = N / 10.]


# def digits_of_anumber():
#     n=32144
#     count=0
#     while(n>0):
#         remainder=n%10
#         n=int(n/10)
#         count+=1
#         print(remainder)
#  digits_of_anumber()



#  Q4. Write a function to return the count the number of digits in a number, n .


# def digits_of_number(n):
#     count=0
#     while(n>0):
#         n=int (n/10)
#         count+=1
#     return count
# n=int(input("Enter a number"))
# print("Number of digits present in ",n," is " , digits_of_number(n))


# Q5. Write a function to return the sum of digits of a number, n .


# def digits_of_number(n):
#     sum=0
#     remainder=0
#     while(n>0):
#         remainder= n%10
#         sum=sum+remainder
#         n=int (n/10)
#     return sum 
# n=int(input("Enter a number"))
# print("Sum of digits present in ",n," is " , digits_of_number(n))


# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.


# print("print all numbers from 1 to 100 that are divisible by both 3 and 5.\n")
# for i in range(1,100,1):
#     if(i%3==0 or i%5==0):
#         print(i)

# Q7.
# Design a program to continuously input a number from user & print if it is
# positive or negative until the user enters “Quit”

# while(True):
#         print("1. For enter a number to check if it iss positive or negative")
#         print("2. Quit")
#         number=int(input("Enter a number: "))
#         def positive_or_negative(num):
#                 if(num > 0):
#                     return ("positive")
#                 else:
#                     return ("nagative")
#         match number:
#                 case 1 :
#                       num=int(input("Enter your number: "))
#                       print("Number is ", positive_or_negative(num))        
#                 case 2:
#                       break                     
#                 case _ :
#                      print("Invalid choice!")     



# Q8 Calculator
#  Let’s create a Simple that performs arithmetic operations. Create
# a function calculator(a, b, operation) that performs addition, subtraction,
# multiplication, or division based on operation the parameter.
# [ operation parameter can have values ‘+’ , ‘-’ , '*’ & ‘/’                    
   

# a=int(input("Enter First nuber : "))
# b=int(input("Enter Second nuber : "))
# operator=input("Enter a operator : ")
# def calculator(a,b,operator):
#     match operator:
#         case '+':
#             return (a+b)
#         case '-':
#             return (a-b)
#         case '*':
#             return (a*b)
#         case '/':
#             return (a/b)
#         case _:
#             return ("Invalid operator")
# print("Answer is ",calculator(a,b,operator))



# Q9 
# Write a function is_prime(n) that returns True n if is a prime number and
# False otherwise, using a loop.
# [Hint -
# 1. We only check prime for 2 or numbers greater than 2. 2 is the smallest
# prime number.
# 2. A non-Prime number, n, will always get divided by atleast one number in
# range [2, n-1].
# Eg - For number 9 we’ll check in range (2, 8) & it’ll get divided by 3. So 9 is
# non-prime & we’ll return false for it.
# For number 7 we’ll check in range (2, 6) & it won’t get divided by any. So 7
# is prime & we’ll return true for it. ]


# def is_prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return "It is not prime"
#     return "It is prime"
# n= int ( input("Enter a number : "))
# print(is_prime(n))



# Q10. Let’s create a “ Number Guessing Game ”. Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:
# • "Too high" if the guess is above the number
# • "Too low" if the guess is below
# • "Correct!" if the guess matches


# print("Number Guessing Game")
# target=59
# while(True):
#     num=int(input(("Guess a number : ")))
#     if(num==target):
#         print("You Guessed it correct!")
#         break
#     elif (num>target):
#         print("The guess number is above the number")
#     else:
#         print("The guess number is below the number")