#!/usr/bin/env python
# coding: utf-8

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[193]:


def is_two(letter):
    if letter == "2" or letter == 2:
        return "True"
    else:
        return "False"
    
is_two("a")
is_two("2")
is_two(2)


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
#     - Assume the input is a single letter in the alphabet. 

# In[194]:


def is_vowel(letter):
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    if letter in vowel:
        return "True"
    else:
        return "False"

is_vowel("t")


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
#     - Assume the input is a single letter in the alphabet. 

# In[42]:


def is_consonant(letter):
    if is_vowel(letter) == "True":
        return "False"
    else:
        return "True"

is_consonant("b")


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
#     - Assume the input is valid

# In[44]:


def capitalize_consonate(word):
    if is_consonant(word[0]) == "True":
        return word.capitalize()
    else:
        return word
    
capitalize_consonate("cat")


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
#     - Assume all the input are valid 
#     - Needs two arguments

# In[45]:


def calculate_tip(tip_percentage, total_bill):
    total_tip = total_bill * tip_percentage
    return total_tip

calculate_tip(0.65, 100)    


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
#     - Assume all the input are valid
#     - Needs two arguments

# In[46]:


def apply_discount(original_price, discount_percentage):
    discounted_price = original_price * (1 - discount_percentage)
    return discounted_price

apply_discount(100, 0.2)


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
#     - Assume all the input are valid

# In[107]:


def handle_commas(number_with_commas):
    number_with_commas = number_with_commas.replace(",","")
    return int(number_with_commas)

handle_commas("1,2,3,4")           


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
#     - Assume the input is valid

# In[57]:


def get_letter_grade(number_grade):
    if number_grade >= 88:
        return "A"
    if number_grade >= 80:
        return "B"
    if number_grade >= 67:
        return "C"
    if number_grade >= 60:
        return "D"
    else:
        return "F"

get_letter_grade(99)


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
#     - Assume all the input is a string

# In[66]:


def remove_vowels(string):
    for i in string:
        if is_vowel(i) == "True":
            string = string.replace(i,"",1)
        else:
            continue
    return string
        
remove_vowels("abcdefg hijklmn opqrst uvwxyz")


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     -for example:
#         - Name will become name
#         - First Name will become first_name
#         - % Completed will become completed
#     - Assume all the input is a string

# In[106]:


def normalize_name(original_name):
    original_name = original_name.strip() # remove leading and trailing whitespace
    for i in original_name:
        if i == " ": 
            original_name = original_name.replace(i,"_",1) 
        if i in [",", "%", "@", ".", "?", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]:
            original_name = original_name.replace(i,"",1)
    return original_name.lower()

normalize_name("   First Name %Completed,.?!@#$%^&*()   ")            


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#     - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#     - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[103]:


def cumulative_sum(list_of_numbers):
    sub_list = []
    cumulative_sum_list = []
    for number in list_of_numbers:
        sub_list.append(number)
        cumulative_sum_list.append(sum(sub_list))
    return cumulative_sum_list

print(cumulative_sum([1,1,1]))
print(cumulative_sum([1,2,3,4]))


# Bonus
# 
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[132]:


def twelveto24(string_is_time):
    if string_is_time.count("am") == 1:
        return string_is_time.replace("am","")
    if string_is_time.count("pm") == 1:
        original_hour = string_is_time[0]
        adjusted_hour = int(original_hour) + 12
        string_is_time = string_is_time.replace(original_hour,"16")
        return string_is_time.replace("pm","")

print(twelveto24("10:45am"))
print(twelveto24("4:30pm"))


# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#     - col_index('A') returns 1
#     - col_index('B') returns 2
#     - col_index('AA') returns 27
#     
# Strategy:
# A = 1
# B = 2
# ...
# Z = 26
# 
# AA = 27 = 26*1 + 1
# AB = 28 = 26*1 + 2
# ...
# AZ = 52 = 26*1 + 26
# BA = 53 = 26*2 + 1
# ...
# DC = 107 = 26*4 + 3 = 107
# ...
# AAA = 703 = (26**2)*1 + (26**1)*1 + 1
# AAB = 704 = 26**2 + 26*1 + 2 = 704
# ALF = 994 = (26**2)*1 + (26**1)*12 + 6 = 994
# ...
# APG = (26**2)*1 + 26*16 + 7 = 1099

# In[175]:


# Step 1: Match each letter with the number using index
# Step 2: Assign each letter a number
# Step 3: Add them together

def letter_to_number(letter):
    letter_number = ["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return letter_number.index(letter)

def col_index(column_name):
    k = len(column_name)
    power = k - 1
    data = []
    for i in column_name:
        num = letter_to_number(i)
        data.append((26**power)*num)
        power = power - 1

    return sum(data)

col_index("ALF")

