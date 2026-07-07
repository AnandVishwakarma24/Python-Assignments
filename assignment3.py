# Python Fundamentals
# (Assignment3)
# Assignment Problems


# Q1. Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is same when we read it forward & backward. Eg -
# “madam”, “racecar” etc.
# [ Hint - A palindrome string is equal to the reversed version of the string. We can
# use a loop to reverse the string manually. ]


# # string="anand"
# string = "madam"
# string=input("Enter a string:")

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# Q2. Given a list of integers compute the average of all numbers in the list.

# list=[1,2,3,4,5,6]
# # print(type(list))
# sum=0
# for val in list:
#     sum+=val
# print(f"Sum of {list} is {sum}")



# Q3. Input two lists of integers from the user. Merge them into one list and sort the result.
# Eg - list1 = [1, 2, 7] , list2 = [2, 4, 5]
# result = [1, 2, 3, 54, 5, 7]


# list1=[]
# list2=[]
# print(type(list1))
# print(type(list2))
# l1=int(input("Enter number of list one : "))
# for i in range(l1):
#     temp=int(input("Enter value : "))
#     list1.append(temp)
# l2=int(input("Enter number of list two: "))
# for i in range(l2):
#     temp=int(input("Enter value : "))
#     list2.append(temp)

# print(list1)
# print(list2)
# result= list1 + list2
# print("Merge List:",result)
# result1=sorted(result)
# print("Sorted list: ",result1)



# Q4. Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers


# tup=(1,2,3,4,5,6,7,8,9,10)
# tuple_odd=()
# print(type(tuple_odd))
# tuple_even=()
# print(type(tuple_odd))
# for i in tup:
#     if(i%2==0):
#         tuple_even+=(i,)
#     else:
#         tuple_odd+=(i,)
# print("ODD tuple : ",tuple_odd)
# print("Even tuple : ",tuple_even)



# Q5. Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
# depending on the operation they want to perform on the dictionary:
# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks


# student_marks={
#     "Anand":  95,
#     "Shilpa": 93
# }
# print(type(dict))
# while True:
#     print("Menu option")
#     print("1. A - Add a student")
#     print("2. B - Update marks")
#     print("3. C - Search for a student")
#     print("4. D - Display all students and marks")
#     choose=input("Choose an option : ")
#     match choose:
#         case 'A' :
#             name=input("Enter student name : ")
#             marks=int(input("Enter marks : "))
#             student_marks.update({"name":"marks"})
#         case 'B' : 
#             name=input("Enter student name : ")
#             marks=int(input("Enter new marks"))
#             # dict.get(name)=marks
#             student_marks.update({"name":"marks"})
#         case 'C' : 
#             name=input("Enter student name : ")
#             print(student_marks.get(name))
#         case 'D' : 
#             for name , marks in student_marks.items():
#                 print(f"The Student name : {name}")
#                 print(f"The Student marks : {marks}")
#         case 'E':
#             print("Thankyou!")
#             break
#         case _ :
#             print("Invalid Choice!")



# Q6. Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}


# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# words_length={}
# print(type(words_length))
# for val in words:
#     length=len(val)
#     words_length[val]=length
# print(words_length)



# Q7
# . Write a program that takes a string from the user and prints the number of
# spaces in the string.


# string1=input("Enter string : ")
# count=0
# for i in string1:
#     if(i==' '):
#         count+=1
# print("The number of spaces into given sting : ",count)



# Q8. Write a program to check whether two lists share no common elements.
# # share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# # share common elements list1 = [1, 2, 3] list2 = [3, 4]
# [Hint - use sets]


# list1 =set([1, 2, 3, 4])
# list2 = set([5, 6, 7, 8])
# list5=list1.intersection(list2)
# print("share no common elements ",list5)
# list3 = set([1, 2, 3]) 
# list4 = set([3, 4])
# list6=list3.union(list4)
# print("share no common elements ", list6)



# Q9. Given a list, print all elements that appear more than once in the list.
# [Hint - use sets]


# list1=[1,2,3,2,4,5]
# seen=set()
# duplicat=set()
# for num in list1:
#     if num in seen:
#         duplicat.add(num)
#     else:
#         seen.add(num)
# print("Dublicate values : ",duplicat)



# Q10. Ask the user for a string and print:
# • All unique characters
# • The count of unique characters


# string1=input("Enter a string : ")
# seen=set()
# duplicat=set()
# for num in string1:
#     if num in seen:
#         duplicat.add(num)
#     else:
#         seen.add(num)
# print("Unique values : ",seen)
# print("Duplicate characters:", duplicat)