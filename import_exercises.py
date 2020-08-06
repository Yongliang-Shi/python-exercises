#!/usr/bin/env python
# coding: utf-8

# 1. Import and test 3 of the functions from your functions exercise file.
# 
#     Import each function in a different way:
# 
#     - import the module and refer to the function with the . syntax
#     - use from to import the function directly
#     - use from and give the function a different name

# In[83]:


# The first function under the test is "is_two"
# Method 1: import the module and refer to the function with the .syntax

import function_exercises

function_exercises.is_two(2)

# Restart kernel
# I need to clean up my function_exercises.py.


# In[ ]:


# Method 2: use FROM TO import the function directly

from function_exercises import is_two

is_two("a")

# Take away: even the function is imported directly, it doesn't mean Python only run the imported function, 
# instead Python run the function_exercises
# Restart kernel


# In[ ]:


# Method 3: use FROM and give the function a different name

from function_exercises import is_two as verify_is_two

verify_is_two("2")

# Restart kernal


# In[ ]:


# The second funtion under test is "cumulative_sum"

# Method 1: import the module and refer to the function with the . syntax

import function_exercises
function_exercises.cumulative_sum([1,2,3,4])

# Restart kernal


# In[ ]:


# Method 2: use FROM to import the function directly

from function_exercises import cumulative_sum

cumulative_sum([1,2,3,4])

# Restart kernal


# In[ ]:


# Method 3: use FROM and give the function a different name

from function_exercises import cumulative_sum as cs

cs([1,2,3,4])

# Restart kernal


# In[ ]:


# The third function under test is "col_index", which contains another function "letter_to_number" in it
# Method 1: import the module and refer to the function with the . syntax

import function_exercises

function_exercises.col_index("ALF")

# Restart kernal


# In[ ]:


# Method 2: use FROM to import the function directly

from function_exercises import col_index

col_index("ALF")

# Restart kernel


# In[ ]:


# Method 3: use FROM and give the function a different name

from function_exercises import col_index as ci

ci("ALF")

# Restart kernel


# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 
# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# 2. How many different ways can you combine two of the letters from "abcd"?

# In[82]:


# Q1: Like a passcode combo, the question is about how many combination for "abc123" or ['a', 'b','c',1,2,3]

from itertools import permutations  
  
n = "abc123"

# no length entered so default length taken as 6(the length of string GeEK) 
p = list(permutations(n))
  
# The number of different ways are the length of list which contains all possible permutations
print(len(p))

# Print out the first 10 in the list 
for i in range(0,10):
    print(p[i])


# In[84]:


# Q2 is asking how many different ways to take two letters from "abcd"
# if the order matters, permutations should be used

n = 'abcd'

p = list(permutations(n,2))

print(len(p))

# if the order doesn't matters, combinations should be used

from itertools import combinations

n = 'abcd'

p = list(combinations(n,2))

print(len(p))


# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information

# In[46]:


from json import load

with open('profiles.json') as users:
    data = load(users)

# valid the profiles.json is a list of dicts
data[5]


# In[85]:


# Total number of users

total_number = len(data)
print(total_number)


# In[20]:


# Number of active users

active_id = [i["_id"] for i in data if i["isActive"] == True]
number_of_active = len(active_id)
print(number_of_active)


# In[21]:


# Number of inactive users

inactive_id = [i["_id"] for i in data if i["isActive"] == False]
number_of_inactive = len(inactive_id)
print(number_of_inactive)


# In[31]:


# Grand total of balances for all users

balances_str = [i["balance"] for i in data]
balances_float = []

for balance in balances:
    balance = balance.replace("$","")
    balance = balance.replace(",","")
    balance = float(balance)
    balances_float.append(balance)

grand_total = sum(balances_float)
print(grand_total)


# In[32]:


# Average balance per user

from statistics import mean

avg_balance = mean(balances_float)
print(avg_balance)


# In[39]:


# User with the lowest balance

lowest_balance = min(balances_float)
number_of_lowest = balances_float.count(lowest_balance)
print(number_of_lowest)
user_position = balances_float.index(lowest_balance)
user_name = data[user_position]["name"]
print(user_name)


# In[43]:


# User with the highest balance

hightest_balance = max(balances_float)
number_of_highest = balances_float.count(hightest_balance)
print(number_of_lowest)
user_position = balances_float.index(hightest_balance)
user_name = data[user_position]["name"]
print(user_name)


# In[74]:


# Most and lesst common favorite fruit

favorite_fruit = [i["favoriteFruit"] for i in data]
types_of_favorite_fruit = set(favorite_fruit)
print(types_of_favorite_fruit) # {'apple', 'banana', 'strawberry'}

f_table = [
    {"favorite_fruit": "apple", "frequency": 0},
    {"favorite_fruit": "banana","frequency": 0},
    {"favorite_fruit": "strawberry","frequency": 0}
]

for fruit in favorite_fruit:
    if fruit == "apple":
        f_table[0]["frequency"] += 1
    if fruit == "banana":
        f_table[1]["frequency"] += 1
    if fruit == "strawberry":
        f_table[2]["frequency"] += 1
        
f_table = sorted(f_table, key = lambda i: i["frequency"])

print(f_table)

print("Least common favorite fruit:", f_table[0]["favorite_fruit"])
print("Most common favorite fruit:", f_table[2]["favorite_fruit"])


# In[81]:


# Total number of unread messages for all users

# The number of unread messages is within the greeting message. 
list_of_greeting = [i["greeting"] for i in data]

# Extract number from the string and combine them together
unread_messages = []
for greeting in list_of_greeting:
    unread_messages += [int(i) for i in greeting.split() if i.isdigit()]

total_number_of_unread = sum(unread_messages)
print(total_number_of_unread)

