# Python Fundamentals

# (Assignment4)

# Assignment Problems



# Concept: Classes & Objects


# Q1 Create BankAccount attributes account_number owner_name, balance.
# Add methods to deposit, withdraw, and check balance.


# class Bank_Account:
#     def __init__(self,account_number, owner_name):
#         self.account_number=account_number
#         self.owner_name=owner_name
#         self.balance=0

#     def deposit(self,deposit):
#         self.balance=self.balance + deposit
#         print(f"{deposit} Balance Deposited Successfully !")

#     def withdraw(self,withdraw):
#          if withdraw<=self.balance:
#             self.balance=self.balance - withdraw
#             print(f"{withdraw} Balance Withdraw Successful !")
#          else:
#             print("Insufficient Balance !")
#     def info(self):
#         print(f"Account Number : {self.account_number} \n Owner Name : {self.owner_name} \n Balance : {self.balance}")

# owner_name=input("Enter Account Holder's Name : ")
# account_number=int(input("Enter Account Number : "))
# acc=Bank_Account(account_number, owner_name)
# while(True):
#     print("-------------------------------")
#     print(" 1. Deposit \n 2. Withdraw \n 3. Account Info \n 4. Exit")
#     choice=int(input("Enter Your Choice : "))

#     print("-------------------------------")
#     if choice==1:
#         deposit=int(input("Enter Amount to Deposit : "))
#         acc.deposit(deposit)
#     elif choice==2:
#         withdraw=int(input("Enter Amount to Withdraw : "))
#         acc.withdraw(withdraw)
#     elif choice==3:
#         acc.info()
#     elif choice==4:
#         break
#     else:
#         print("Invalid Choice !")



# Concept: Classes & Objects


# Q2. Create a class Book with the following attributes:
# • title
# • author
# • list of reviews
# And add methods to:
# • add a new review
# • count reviews
# • display all reviews

# class Book:
#     def __init__(self,title,auther):
#         self.title=title
#         self.auther=auther
#         self.reviews=[]
#     def add_review(self,review):
#         self.reviews.append(review)
#         print("Review added successfully!")
#     def count_review(self):
#         print("Total Number of review : ",len(self.reviews))
#     def display_review(self):
#         print("Reviews :")
#         for rev in self.reviews:
#             print(rev)

# title = input("Enter Book Title: ")
# author = input("Enter Author Name: ")

# book = Book(title, author)

# while True:
#     print("-------------------------------")
    
#     print("\n1. Add Review")
#     print("2. Count Reviews")
#     print("3. Display Reviews")
#     print("4. Exit")

#     choice = int(input("Enter Your Choice: "))
#     print("-------------------------------")

#     if choice == 1:
#         review = input("Enter Review: ")
#         book.add_review(review)

#     elif choice == 2:
#         book.count_review()

#     elif choice == 3:
#         book.display_review()

#     elif choice == 4:
#         print("Thank You!")
#         break

#     else:
#         print("Invalid Choice!")



# Concept: Encapsulation

  
# Q3.Create a class Student with private attributes _name, _roll_no, and _marks.
# Provide getter and setter methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 & 100 & name cannot be empty).

# class Student:
#     def __init__(self,name,roll_number,marks):
#         self.__name=name
#         self.__roll_number=roll_number
#         self.__marks=marks
#     def get_name(self):
#         return self.__name
#     def get_roll_number(self):
#         return self.__roll_number
#     def get_marks(self):
#         return self.__marks
#     def set_name(self,new_name):
#         if new_name!='':
#             self.__name=new_name
#         else:
#             print("Invalid Name !")
#     def set_marks(self,new_marks):
#         if new_marks>=0 and new_marks<=100:
#             self.__marks=new_marks
#         else:
#             print("Invalid marks !")
#     def set_roll_number(self,new_roll_number):
#         if new_roll_number>0 and new_roll_number<101:
#             self.__roll_number=new_roll_number
#         else:
#             print("Invalid Enrollment Number !")

# flag=1
# while(flag==1):
#     name = input("Enter Student Name : ")
#     roll_number = int(input("Enter Student Enrollment Number : "))
#     marks=int(input("Enter Student Marks : "))

#     if(name=="" or roll_number<=0 or roll_number>=101 or marks<0 or marks>100):
#         print("Invalid Input !")
#         continue

#     student_info = Student(name, roll_number, marks)

#     while True:
#         print("-------------------------------")
        
#         print("\n1. Edit Information")
#         print("2. Display Student Information ")
#         print("3. Exit ")

#         choice = int(input("Enter Your Choice: "))
#         print("-------------------------------")

#         if choice == 1:
#             while (True):
#                 print("Edit options ")
#                 print("1. Edit Name")
#                 print("2. Edit Enrollment Number")
#                 print("3. Edit Marks")
#                 print("4. Exit")
#                 choice = int(input("Enter Your Choice: "))
#                 if choice == 1:
#                     name=input("Enter New Name : ")
#                     student_info.set_name(name)
#                 elif choice == 2:
#                     roll_number=int(input("Enter New Enrollment Number : "))
#                     student_info.set_roll_number(roll_number)
#                 elif choice == 3:
#                     marks=int(input("Enter New Marks : "))
#                     student_info.set_marks(marks)
#                 elif choice ==4:
#                     print("Exiting.......")
#                     break
#                 else:
#                     print("Invalid Choice !")
#         elif choice == 2:
#             print(f" Name : {student_info.get_name()} \n Enrollment Number : {student_info.get_roll_number()} \n Marks : {student_info.get_marks()}")

#         elif choice == 3:
#             print("Thank You!")
#             flag=0
#             break

#         else:
#             print("Invalid Choice!")



# Concept: Function Overriding


# Q4. Create a class Shape with a method area().
# Create subclasses Circle, Rectangle, and Triangle that override the area() method.

# class shape: 
#     def area(self):
#         print("Area of shape is not define")

# class Rectangle(shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return print("Area of the Rectangle : ",self.length*self.width)
# class Circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return print("Area of the Circle : ",self.radius*3.14)
# class triangle(shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return print("Area of the Triangle : ",self.height*self.base*0.5)

# shap1=Rectangle(23,22)
# shap2=Circle(44)
# shap3=triangle(32,22)
# shap1.area()
# shap2.area()
# shap3.area()



# Concept: Inheritance


# Q5. Create a  base class Vehicle with attributes like brand and model.
# Create two subclasses Car and Bike that add extra attributes - seats (in Car) & engine_cc (in Bike).

# class Vehicle:
#     def __init__(self,brand,model):
#         self.model=model
#         self.brand=brand
# class Car(Vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand,model)
#         self.seats=seats
#     def display(self):
#         print(f"The {self.model} of {self.brand} Car  have {self.seats} seats available ")
# class Bike(Vehicle):
#     def __init__(self,brand,model,engine_cc):
#         super().__init__(brand,model)
#         self.engine_cc=engine_cc
#     def display(self):
#         print(f"The {self.model} of {self.brand} Bike have {self.engine_cc} cc engine")

# car1=Car("Maruti","Swift",5)
# bike1=Bike("Honda","Shine",125)
# car1.display()
# bike1.display()



# Concept: Abstraction


# Q6. Create an abstract class  Employee with an abstract method
# calculate_salary().
# Create subclasses  Intern, FullTimeEmployee, and  ContractEmployee
# that implement the method differently.

# from abc import ABC,abstractmethod
# class employee (ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         print("NO salary define")
#         pass
# class intern(employee):
#     def calculate_salary(self):
#         print("Intern salary is 5000/month")

# class full_Time_Employee(employee):
#     def calculate_salary(self):
#         print(f"Full Time Employee salary is 30_000/month")
# class Contract_Employee(employee):
#     def calculate_salary(self):
#         print(f"Contract Employee salary is 20_000/month")

# intern1=intern()
# intern1.calculate_salary()

# Contract_employee1=Contract_Employee()
# Contract_employee1.calculate_salary()

# full_Time_Employee1=full_Time_Employee()
# full_Time_Employee1.calculate_salary()



# Concept: Constructor Overloading (with Default Parameters)


# Q7. Create a class Person that allows the constructor to work with:
# • name only
# • name + age
# • name + age + address
# As direct constructor overloading (multiple constructors) are not allowed but
# we have to use default parameters to simulate constructor overloading.

# class person:
#     def __init__(self,name):
#         self.name=name
#     def get_info(self):
#         print(f"Name : {self.name}")
# class person1(person):
#     def __init__(self,name,age=0):
#         super().__init__(name)
#         self.age=age
#     def get_info(self):
#         super().get_info()
#         print(f"Age : {self.age}")
# class person2(person1):
#     def __init__(self,name,age=0,address=""):
#             super().__init__(name,age)
#             self.address=address
#     def get_info(self):
#         super().get_info()
#         print(f"Address : {self.address}")

# p1 = person("Anand")
# p1.get_info()

# p2 = person1("John", 30)
# p2.get_info()

# p3 = person2("Jane", 25, "123 Main St")
# p3.get_info()



# Concept: Instance & Class Attributes


# Q8. Create a class Player with:
# • a class variable player_count
# • instance variables name and level
# Track how many players were created.

# class player:
#     count=0
#     def __init__(self,name,level):
#         self.name=name
#         self.level=level
#         player.count+=1
#     def display(self):
#         print("Name : ",self.name)
#         print("Level : ",self.level)

# p1=player("Anand",100)
# p1.display()

# p2=player("Vishal",99)
# p2.display()
# print("Total Players Created:", player.count)



# Concept: Multiple Inheritance


# Q9. Create the following classes: Herbivore, Carnivorn, with Omnivore some
# attributes & methods. Then create a class Bear that inherits from all the above
# classes to showcase how multiple inheritance works.

# class Herbivore:
#     def __init__(self):
#         self.herb_food="Plants"
#     def eat_plants(self):
#         print(f"Herbivore eats : {self.herb_food}")
# class Carnivor:
#     def __init__(self):
#         self.carn_food="Meat"
#     def eat_meat(self):
#         print(f"Carnivor eats : {self.carn_food}")
# class Omnivore:
#     def __init__(self):
#         self.type="Omnivore"
#     def eat_type(self):
#         print("Omnivore eats both plant and meat.")
# class bear(Herbivore,Carnivor,Omnivore):
#     def __init__(self):
#         Herbivore.__init__(self)
#         Carnivor.__init__(self)
#         Omnivore.__init__(self)
#         self.name = "Bear"

#     def display(self):
#         print("Animal Name:", self.name)

# b = bear()

# b.display()
# b.eat_plants()
# b.eat_meat()
# b.eat_type()



# Concept: OOP


# Q10. Mini Project – OOP Chat System
# Let’s create a Chat System using OOPs concepts. We have to create classes:
# • User
# • Message
# • ChatRoom
# And we have to implement functions:
# • sending messages
# • viewing chat history
# • user joining and leaving the chatroom

# class User:
#     def __init__(self,name):
#         self.name=name
#     def send_message(self, chatroom, text):
#         chatroom.add_message(self,text)
#     def join_chat(self, chatroom):
#         chatroom.join_user(self)
#     def leave_chat(self,chatroom):
#         chatroom.leave_user(self)

# class Message:
#     def __init__(self,sender,text):
#         self.sender=sender
#         self.text=text
#     def display(self):
#         print(f"{self.sender} : {self.text}")

# class ChatRoom:
#     def __init__(self,room_name):
#         self.room_name=room_name
#         self.users=[]
#         self.messages=[]
#     def join_user(self,user):
#         if user not in self.users:
#             self.users.append(user)
#             print(f"{user.name} joined '{self.room_name}'.")
#     def leave_user(self, user):
#         if user in self.users:
#             self.users.remove(user)
#             print(f"{user.name} left '{self.room_name}.'")
#     def add_message(self, user, text):
#         if user in self.users:
#             message=Message(user.name,text)
#             self.messages.append(message)
#             print(f"Message sent by {user.name}")
#         else:
#             print(f"{user.name} is not in the chat room!")
#     def show_chat_history(self):
#         print(f"\n---Chat History of {self.room_name}")
#         if not self.messages:
#             print("No message yet.")
#         else:
#             for message in self.messages:
#                 message.display()

# room=ChatRoom("Python Leaners")

# user1=User("Anand")
# user2=User("Vishal")
# user3=User("Rahul")


# user1.join_chat(room)
# user2.join_chat(room)


# user1.send_message(room ,"Hi Vishal!")
# user2.send_message(room, "Hi Anand!")

# user2.leave_chat(room)

# user2.send_message(room, "Can anyone hear me!")

# user3.join_chat(room)
# user3.send_message(room, "Hello friends!")

# room.show_chat_history()

