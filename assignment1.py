# Python Fundamentals
# (Assignment1)
# Assignment Problems



# Q1. Write a program that asks the user for their name and age, then prints a
# sentence like:
# Hello Shradha, you are 21 years old!


# name=input("Enter your name : ")
# age= int(input("Enter your age : "))
# print(f"Hello {name}, you are {age} years old!")



# Q2. Take two numbers as input from the user and print their sum, difference,product, and quotient.


# num1=int(input("Enter first number : "))
# num2=int(input("Enter second number : "))
# print(f"Sum of given two number : {num1+num2}")
# print(f"Difference of given two number : {num1-num2}")
# print(f"Product of given two number : {num1*num2}")
# print(f"Quotient of given two number : {num1%num2}")



# Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.


# num1=int(input("Enter Integer number : "))
# num2=float(input("Enter Float number : "))
# avg=float((num1+num2)/2)
# print(f"The average of the two numbers in float : {avg}")



# Q4. The user enters a string containing a number (e.g., "45" ). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.


# string1=input("Enter a number")
# print("The type of given string : ",type(string1))
# print("Converted into an integer : ",int(string1))
# print("Converted into an float : ",float(string1))
# print("Converted into an string : ",str(string1))



# Q5. Evaluate and print the result of the following expression:
# x = 10 + 3 * 2 ** 2
# Based on what you learnt in the lecture explain why the output is what it is.


# print(x)   //Answer:22



# Q6. Write a program to swap values of two numbers entered by the user.


# num1=int(input("Enter first number : "))
# num2=int(input("Enter second number : "))
# temp=0
# temp=num1
# num1=num2
# num2=temp
# print(f"After swap first number is {num1} and second number is {num2}" )



# Q7. Ask the user for a temperature in Celsius (string input). Convert it to float,
# then calculate and print temperature in Fahrenheit.
# Conversion formula:  FahrenheitTemp= (CelsiusTemp ∗ (9/5)) + 32


# celsius=float(input("Enter temperature in celsius : "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit : ",fahrenheit)



# Q8. Take the radius (r) as user input and print the area.
# Use the formula: Area = π * r2 (value of π = 3.14)


# rad=float(input("Enter radius : "))
# area=3.14 * rad *rad
# print("Area of given radius : ", area)



# Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest:


# principal=float(input("Enter principle amount : "))
# rate=float(input("Enter rate : "))
# time=float(input("Enter Time: "))
# SI=(principal*rate*time)/100
# print("Simple Interest is : ",SI)



# Q10. Take a decimal number as input (like 45.78 ) and output its:
# • integer part - 45
# • fractional part - .78


# num=input("Enter first number : ")
# print("Integer part : ",int(num))
# fractional_part = num- int(num)
# print("Fractional part : ",fractional_part)