#!/usr/bin/env python
# coding: utf-8

# # 1. Conditional Basics

# In[73]:


# a. prompt the user for a day of the week, print out whether the day is Monday or not
input_day = input("Please type a day of the week: ")
if input_day.capitalize() == "Monday":
    print("It is Monday")
else:
    print("It is not Monday")


# In[75]:


# How to determine what day it is today?

import datetime
datetime.datetime.today()
datetime.datetime.today().weekday()

if datetime.datetime.today().weekday() == 0:
    print("Today is Monday")
else:
    print("Today is not Monday")


# In[76]:


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

user_day = input("Please type a weekday:")
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if user_day.capitalize() in weekday:
    print("It is a Weekday")
elif user_day.capitalize() in weekend:
    print("It is a Weekend")
else:
    print("Invalid input")


# In[19]:


# c. create variables and make up values for
    # the number of hours worked in one week
    # the hourly rate
    # how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

work_hours = 20
hourly_rate = 20

if 0 <= work_hours <= 40:
    week_pay = work_hours * hourly_rate
elif 40 < work_hours <= 7*24:
    week_pay = 40 * hourly_rate + (work_hours - 40) * hourly_rate * 1.5
elif work_hours > 7*24:
    week_pay = "Are you from Mars?"
else:
    week_pay = "You'd better start work"

print(week_pay)


# # 2. Loop Basics 

# In[24]:


# a. While
    # Create an integer variable i with a value of 5.
    # Create a while loop that runs so long as i is less than or equal to 15
    # Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1


# In[25]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2


# In[31]:


# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5    


# In[39]:


# Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000. Output should equal:

i = 2
while i <= 1000000:
    print(i)
    i = i * i


# In[41]:


# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5


# In[19]:


# It is very convenient to generate arithmetic and geometric progression
i = 100
n = []
while i >= 5:
    n.append(i)
    i -= 5
print(n)


# In[58]:


# i. Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

num = int(input("Type in a : "))

for i in range (1,11):
    print(f"{num} x {i} = {num*i}")


# In[11]:


# ii. Create a for loop that uses print to create the output shown below.
# use "1"*i to generate "111...", then conver it to int

for i in range(1,10):
    print(int("1"*i)*i)


# C. break and continue
# 
# i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. Hint: use the isdigit method on strings so determine this. Use a loop and continue statement to output all the odd numbers between 1 and 50, except for the number the user entered. 

# In[7]:


# Step 1: use WHILE to create a list of odd number between 1 and 50

odd_number = []
n = 1
while n < 50:
    odd_number.append(n)
    n += 2
print(odd_number) # list is correct


# In[ ]:


# Step 2: validate the input (user_input can be any data type: int, float, boolean, list, dict, etc.)

user_input = input("Enter an odd number between 1 and 50: ")
type(user_input) # No matter what the user input, the datatype that INPUT returns is str.


# In[122]:


# Test .isdigit()

# .isdigit() return flase if the string input is negative or a float

print("5".isdigit())
print("-5".isdigit())
print("4.5".isdigit())

# .isdecimal() returns false if the string input is negative or a float

print("5".isdecimal())
print("-5".isdecimal())
print("4.5".isdecimal())

# .isnumeric() also returns false if the string input is negative or a floast

print("5".isnumeric())
print("-5".isnumeric())
print("4.5".isnumeric())

# int() is a good tool to convert string to integer when the string input is "integer" but
# it returns ValueError when the string input is "float"
int("4")


# In[40]:


# Limited input vs. Unlimited input

# Limited input: the users are given 3 chances to enter the number.

user_input = input("Enter an odd number between 1 and 50: ")

for i in range(0,4):
    if i == 3:   # this is 4th time the user trys to input
        print("Please call xxx-xxx-xxxx to regain the access")
        break
    if user_input.isdigit() == False or int(user_input) < 1 or int(user_input) >= 50 or int(user_input)%2 != 1:
        print(f"Not Valid and {2-i} times left")
        user_input = input("Enter an odd number between 1 and 50: ")
    else:
        print("Valid")
        break


# In[12]:


# Unlimited input: 

user_input = input("Enter an odd number between 1 and 50: ")

while user_input.isdigit() == False or int(user_input) < 1 or int(user_input) >= 50 or int(user_input)%2 != 1:
    print("Not Valid")
    user_input = input("Enter an odd number between 1 and 50: ")


# In[1]:


# Step 3: output all odd number between 1 and 50, except the number the user input

user_input = input("Enter an odd number between 1 and 50: ")

odd_number = []
n = 1
while n < 50:
    odd_number.append(n)
    n += 2

while user_input.isdigit() == False or int(user_input) < 1 or int(user_input) >= 50 or int(user_input)%2 != 1:
    print("Not Valid")
    user_input = input("Enter an odd number between 1 and 50: ")

for num in odd_number:
    if num == int(user_input):
        print(f"Yikes! Skipping number: {num}")
#         continue
    else:
        print(f"Here is an odd number: {num}")


# d. The INPUT function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the INPUT function returns a string, so you'll need to convert this to a numeric type.

# In[1]:


input_int = input("Please type in an positive integer: ")

while input_int.isdigit() == False:
    input_int = input("Please type in an integer: ")

num_count = [n for n in range(0,int(input_int)+1)]
print(num_count)

# How about positive float, like 4.5? 


# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[51]:


input_int = input("Please type in an positive integer: ")

while input_int.isdigit() == False:
    input_int = input("Please type in an integer: ")

num_count = [n for n in range(1,int(input_int)+1)]
num_count.reverse()
print(num_count)


# # Q3: Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# In[53]:


# Write a program that prints the numbers from 1 to 100.

num = []
for i in range(1, 101):
    num.append(i)
print(num)

# You can also use list comprehension


# In[57]:


# For multiples of three print "Fizz" instead of the number

user_input = input("Please tyep in a number: ")

if user_input.isdigit() and (int(user_input)%3 == 0):
    print("Fizz")
else:
    print("invalid")    


# In[59]:


# For the multiples of five print "Buzz".
user_input = input("Please tyep in a number: ")

if user_input.isdigit() and (int(user_input)%5 == 0):
    print("Buzz")
else:
    print("invalid")    


# In[60]:


# For numbers which are multiples of both three and five print "FizzBuzz".

user_input = input("Please tyep in a number: ")

if user_input.isdigit() and (int(user_input)%3 == 0) and (int(user_input)%5 == 0):
    print("FizzBuzz")
else:
    print("invalid")  


# # Q4: Display a table of powers.

# In[9]:


# Use TRY EXCEPT for the string input validation
#     type(int("float or contains string")) returns ValueError

try:
    user_input = int(input("What number would you like to go up to?"))
    print()
    print("Here is your table!")
    print()
except ValueError: 
    print("Invalid entry.")

# Calculate the squares and cubes of the input and put them in a list

filed_names = ["number", "squared", "cubed"]

# print(data_list) # valid

print("number| squared| cubed")
print("-"*20)

for i in range(0,user_input):
    print('{:<6}|'.format(f"{(i+1)}"),'{:<7}|'.format(f"{(i+1)**2}"),'{:<7}'.format(f"{(i+1)**3}"))
    print()
    
# Add continuing prompting

do_it_again = input("Do you want to continue? Please type Y/N")

if do_it_again == "Y":
    user_input = input("Pleaese enter a numerical grade: ")
    user_input = int(user_input)


# In[18]:


# Use WHILE LOOP to combine them together

user_input = "Y"

while user_input == "Y": 
    user_input = int(input("What number would you like to go up to?"))
    print("number| squared| cubed")
    print("-"*20)
    for i in range(0,user_input):
        print('{:<6}|'.format(f"{(i+1)}"),'{:<7}|'.format(f"{(i+1)**2}"),'{:<7}'.format(f"{(i+1)**3}"))
        print()
    user_input = (input("Do you want to continue? Please type Y/N"))


# # Q5: Convert given number grades into letter grades

# In[ ]:


#Prompt the user for a numerical grade from 0 to 100.

num_grade = input("Pleaese enter a numerical grade: ") #valid
num_grade = int(num_grade)

# Display the corresponding letter grade

if 88 <= num_grade <=100:
    print("A")
elif 80 <= num_grade <=87:
    print("B")
elif 67 <= num_grade <=79:
    print("C")
elif 60 <= num_grade <= 66:
    print("D")
elif 0 <= num_grade <= 59:
    print("F")

# Prompt the user to continue

do_it_again = input("Do you want to continue? Please type Y/N")

if do_it_again == "Y":
    num_grade = input("Pleaese enter a numerical grade: ")
    num_grade = int(num_grade)


# In[57]:


# Use the LOOP to make the continuing prompting

num_grade = input("Pleaese enter a numerical grade: ")
num_grade = int(num_grade)

if 88 <= num_grade <=100:
    print("A")
elif 80 <= num_grade <=87:
    print("B")
elif 67 <= num_grade <=79:
    print("C")
elif 60 <= num_grade <= 66:
    print("D")
elif 0 <= num_grade <= 59:
    print("F")
    
do_it_again = input("Do you want to continue? Please type Y/N")

while do_it_again == "Y":
    num_grade = input("Pleaese enter a numerical grade: ")
    num_grade = int(num_grade)
    if 88 <= num_grade <=100:
        print("A")
    elif 80 <= num_grade <=87:
        print("B")
    elif 67 <= num_grade <=79:
        print("C")
    elif 60 <= num_grade <= 66:
        print("D")
    elif 0 <= num_grade <= 59:
        print("F")    
    do_it_again = input("Do you want to continue? Please type Y/N")


# In[19]:


# Simplify the coding:

num_grade = "Y"

while num_grade == "Y":
    num_grade = input("Pleaese enter a numerical grade: ")
    num_grade = int(num_grade)
    if 88 <= num_grade <=100:
        print("A")
    elif 80 <= num_grade <=87:
        print("B")
    elif 67 <= num_grade <=79:
        print("C")
    elif 60 <= num_grade <= 66:
        print("D")
    elif 0 <= num_grade <= 59:
        print("F")    
    num_grade = input("Do you want to continue? Please type Y/N")


# # Q6: Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, auther and genre. Loop through the list and print out information about each book.
# # Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[56]:


# create a list of dicts

book_shelf = [
    {"title": "President of America", 
     "auther": "Jon Roper", 
     "genre": "history"},
    {"title": "Marketer's Toolkit", 
     "auther": "Richard Luecke", 
     "genre": "economy"},
    {"title": "Probability for Risk Management 2", 
     "auther": "Hassett Stewart", 
     "genre": "math"},
]

for i in range(0,3):
    print(book_shelf[i])

# Prompt the user to enter a genre

enter_genre = input("Please enter a genre:")

# Loop through your books list and print out the titles of all the books in that genre

for i in range(0,3):
    if enter_genre == book_shelf[i]["genre"]:
        print(book_shelf[i]["title"])
    else:
        continue

