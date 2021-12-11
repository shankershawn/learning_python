# name = input("Please enter your name: ")
# age = input("Hi " + name + ", please enter your age: ")
# isNewPatient = input("Is this your first visit here? ")
# favColor = input(name + ", please tell us your favorite color: ")
# print("Let it be known that " + name + " likes " + favColor + " color.")
#
# weight_in_pounds = float(input("Enter weight in pounds: "))
# print("Weight in kilograms is " + str(0.454 * weight_in_pounds))
#
# course = 'Python\'s Beginner Course'
# print(course)
# message ='''Hi Tapna,
#
# How are you?
#
# Thanks,
# Bikrom'''
# print(message)
########################################
# course = "Hello world"
# print(course[0:4])
# print(course[-5:-3])
# print(course[:])
# print(course[1:-1])
########################################
# first_name = "Poom"
# last_name = "Ganai"
# message = f"{first_name} {last_name} is a good girl."
# print(message)
########################################
# course = "Barnamala for Poom"
# print(len(course))
# print(course.upper())
# print(course)
# print(course.find("for"))
# print(course.find("a"))
# print(course.find("Z"))
# print(course.replace("a","e"))
# print(course.replace("P", "J"))
# print("Poom" in course)
########################################
# print(10 +3)
# print(10/3)
# print(10//3)
# print(10%3)
# x = 4
# x += 3
# print(x)
# print(10 / (3 + 4) ** 2)

# x = 2.9
# print(round(x))
# print(round(abs(-2.9)))


# #######################################


# # import math

# # print(math.floor(3.4))


# ######################################

# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
########################################
# price = 1000000
# is_buyer_credit_good = False
# if is_buyer_credit_good:
#     down_payment = 10 / 100 * price
# else:
#     down_payment = 20 / 100 * price
# print(f"Down payment is {down_payment}")
########################################
# has_high_income = True
# has_good_credit = False
# has_criminal_record = True
# if (has_high_income or has_good_credit) and not has_criminal_record:
#     print("Eligible for loan")
########################################
# temp = float(input("Please enter temperature (in celcius): "))
# if temp > 30.0:
#     print("It's a hot day")
# elif temp < 10.0:
#     print("It's a cold day")
# else:
#     print("It's neither hot nor cold")
########################################
# name = input("Enter your name: ")
# length = len(name)
# if length < 3:
#     print("Name must be at least 3 characters")
# elif length > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good!")
########################################
# weight = input("Enter your weight: ")
# if(weight.isnumeric()):
#     weight = float(weight)
#     unit = input("(L)bs or (K)g: ")
#     if(unit.upper() == "L"):
#         print(f"You are {round(0.454 * weight)} kilos")
#     elif(unit.upper() == "K"):
#         print(f"You are {round(weight / 0.454)} pounds")
#     else:
#         print("You have entered wrong option")
# else:
#     print("Please enter only numerics for weight")
########################################
# i = 1
# while i <=5:
#     print("*" * i)
#     i = i + 1
# print("Done")
########################################
# secret_number = 9
# guess_counter = 0
# guess_limit = 3
# while guess_counter < guess_limit:
#     guess = int(input("Guess: "))
#     guess_counter += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("You failed")
########################################
# command = ""
# started = False
# while True:
#     command = input(">").lower()
#     if "help" == command:
#         print("""start - to start the car
# stop - to stop the car
# quit - to exit""")
#     elif "start" == command:
#         if started:
#             print("Car already started")
#         else:
#             started = True
#             print("Car started...Ready to go!")
#     elif "stop" == command:
#         if not started:
#             print("Car already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif "quit" == command:
#         print("Bye")
#         break
#     else:
#         print("I don't understand that")

########################################
# prices = [10, 20, 30]
# sum = 0
# for item in prices:
#     sum += item
# print(sum)
########################################
# for x in range(4,8):
#     for y in  range(5,10):
#         print(f"({x},{y})")
########################################
# numbers = [5,2,5,2,2]
# for line_length in numbers:
#     print("X" * line_length)
########################################
# names = ["John", "Bob", "Mosh", "Poom", "Tutul"]
# print(names[3])
# print(names[4])
# print(names[-2:]
# for item in names:
#     index = names.index(item)
#     print(names[index -len(names)] == names[index])
########################################
# numbers = [4, 10, -5, 7, 0, -10]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(f"Largest number is {largest}")
########################################
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(numbers[0])
# print(numbers[1])
# print(numbers[-1])
# print(numbers[2][2])
# for row in numbers:
#     for number in row:
#         print(f"Current number is {number}")
########################################
# numbers = [5, 2, 7, 1, 0, 5]
# print(numbers)
# numbers.append(-1)
# print(numbers)
# numbers.insert(3, -4)
# print(numbers)
# numbers.remove(2)
# print(numbers)
# print(numbers.count(5))
# numbers.pop(5)
# print(numbers)
# print(numbers.index(7))
# print(50 in numbers)
# print(1 in numbers)
# print(numbers.count(0))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# numbers2.append(19)
# print(numbers)
# print(numbers2)
########################################
# numbers = [8, 5, -3, 1, -9, 3, 8, -3, 2, -9]
# print(f"Original list is {numbers}")
# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)
#         print(f"Removed {number}")
# print(f"Updated list is {numbers}")

########################################
###### tuples ########
# numbers = (1, 2, 3,)
# print(numbers.index(1))
# print(numbers.count(3))
########################################
##### unpacking #####
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates # same as 3 lines above
# print(f"({x}, {y}, {z})")

########################################
## Dictionaries ####
# customer = {
#     "name": "John Smith",
#     "age": 40,
#     "is_verified": True
# }
# print(customer["name"])
# print(customer.get("dob"))
# print(customer.get("dob", "Jan 1 1989"))
# customer["dob"] = "Feb 2 1989"
# print(customer)
########################################
# digitDictionary = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# number = input("Enter phone number: ")
# word = []
# if number.isnumeric():
#     for digit in number:
#         word.append(digitDictionary[digit])
#     print(" ".join(word))
# else:
#     print("Please enter numeric only")

# message = input("> ")
# words = message.split(" ")
# emoji_dictionary = {
#     ":)": "smiley",
#     ":(": "sad"
# }
# for word in words:
#     message = message.replace(word, emoji_dictionary.get(word, word))
# print(message)
########################################

#### Functionss ####
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user("Mary", "Kom")
# greet_user("Poom", "Ganai") # positional arguments
# greet_user(last_name="fsd", first_name="ddwi") #keyword arguments
# print(greet_user("Poom", last_name="Smith")) # method returns None by default
# print("Finish")

########################################

# def square(number):
#     return number * number
#
#
# number = input("Enter a number to be squared: ")
# if number.isnumeric():
#     print(f"Square of {number} is {square(int(number))}")
# else:
#     print("Please enter only digits!")

########################################

### function reuse #####
# def emoji_convertor(message):
#     words = message.split(" ")
#     emoji_dictionary = {
#         ":)": "happy",
#         ":(": "sad"
#     }
#     for word in words:
#         message = message.replace(word, emoji_dictionary.get(word, word))
#     return message
#
# message = input("> ")
# print(emoji_convertor(message))

########################################

### Error Handling ###
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(f"Age is {age}. Risk is {risk}")
# except ValueError:
#     print("Invalid value. Please enter only numerical values")
# except ZeroDivisionError:
#     print("Division by zero!")
########################################

#### Comments ####
# print("Sky is blue") #Universal Truth <- This is a comment

########################################

### Classes ####

# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point = Point()
# point.move()
# point.x = 10 # can add attributes anywhere in the program
# point.y = 20
# print(point.x)
# point.draw()
#
# point1 = Point()
# point1.x = 50
# print(point1.x)
########################################
### Constructors ###

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point = Point(10, 20)
# point.y = 50
# print(f"({point.x}, {point.y})")

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def do(self, action):
#         if "talk" == action.lower():
#             print(f"{self.name} is talking!!!")
#         elif "laugh" == action.lower():
#             print(f"{self.name} is laughing!!!")
#         elif "cry" == action.lower():
#             print(f"{self.name} is crying!!!")
#
#
# person1 = Person("John")
# person2 = Person("Poom")
# person3 = Person("Babu")
# person1.do("Talk")
# person2.do("Cry")
# person3.do("laugh")
########################################

### Inheritance ###
# class Mammal:
#     def walk(self):
#         print("Walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     def purr(self):
#         print("purr")
#
#
# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.walk()
# dog1.bark()
# cat1.purr()

########################################

### Modules ###

#methods moved to converters.py
# import converters
# from converters import kg_to_lbs
# print(converters.lbs_to_kg(1000))
# print(kg_to_lbs(250)) #using specific portion

# import utils
#
# numbers = [-9, 0, 4, -10, 2, 5]
# utils1 = utils.Utils()
# print(utils1.find_max(numbers))
# print(max(numbers)) # built in method to get max number in a list

########################################

### Packages ###

#import ecommerce.shipping as es
#from ecommerce.shipping import calc_shipping
# from ecommerce import shipping as s
# s.calc_shipping()
# es.calc_shipping()

########################################

### Built-in modules ###

# import random
#
# for i in range(3):
#     print(random.randint(10, 20))
#
# members = ["John", "Poom", "Babu"]
# leader = random.choice(members)
# print(leader)


# from dice import Dice
#
# dice = Dice()
# print(dice.roll())

########################################

### Working with directories ###

from pathlib import Path

# path = Path("email")
# if(not path.exists()):
#     print(path.mkdir())
# print(path.rmdir())
# path = Path()
# print(path.glob("*.py"))
# for file in path.glob("*"):
#     print(file)

########################################

### Working with Excel ###

# import openpyxl as xl
# from openpyxl.chart import BarChart as BC, Reference
#
# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb["Sheet1"]
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * .9
#         print(corrected_price)
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet,
#                        min_row=2,
#                        max_row=sheet.max_row,
#                        min_col=4,
#                        max_col=4)
#
#     chart = BC()
#     chart.add_data(values)
#     sheet.add_chart(chart, "e2")
#     wb.save(filename)
#
# process_workbook("transactions.xlsx")

########################################

### Machine Learning ###

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# music_data = pd.read_csv("music.csv")
# x = music_data.drop(columns=["genre"])
# y = music_data["genre"]
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# model = DecisionTreeClassifier()
# model.fit(x_train, y_train)
# predictions = model.predict(x_test)
#
# score = accuracy_score(y_test, predictions)
# print(str(score))

########################################3

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.externals import joblib
# import joblib
# from sklearn.metrics import accuracy_score
# music_data = pd.read_csv("music.csv")
# x = music_data.drop(columns=["genre"])
# y = music_data["genre"]
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# model = DecisionTreeClassifier()
# model.fit(x_train, y_train)
# model.fit(x, y)
# predictions = model.predict(x_test)
# print(x_train)
# score = accuracy_score(y_test, predictions)
# print(str(score))
# joblib.dump(model, "music-recommender.joblib")
# model = joblib.load("music-recommender.joblib")
# predictions = model.predict([[21,1]])

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn import tree
#
# music_data = pd.read_csv("music.csv")
# x = music_data.drop(columns=["genre"])
# y = music_data["genre"]
#
# model = DecisionTreeClassifier()
# model.fit(x, y)
#
# tree.export_graphviz(model, out_file="music-recommender.dot",
#                     feature_names=["age", "gender"],
#                     class_names=sorted(y.unique()),
#                     label="all",
#                     rounded=True,
#                     filled=True)


#########################################################

#### Web Development with Django ####

