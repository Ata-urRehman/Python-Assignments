#!/usr/bin/env python
# coding: utf-8

# In[9]:


#. Make a calculator using Python with addition , subtraction , multiplication ,division and power.

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')


# In[21]:


#. Write a Python script to check if a given key already exists in a dictionary

Dictionary = {'Mon':3,'Tue':5,'Wed':6,'Thu':9}
print("The given dictionary : ",Dictionary)
check_key = "Fri"
if check_key in Dictionary:
   print(check_key,"is Present.")
else:
   print(check_key, " is not Present.")


# In[20]:


#. Write a program to identify duplicate values from list.

list = [1,2,3,4,5,2,3,4,7,9,5]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
    else:
        print(i,end=' ')


# In[19]:


#. Write a Python program to sum all the numeric items in a dictionary.

Dictionary = {'A':100,'B':540,'C':239}

print("Total sum of values in the dictionary:")

print(sum(Dictionary.values()))


# In[22]:


#. Write a Python script to add a key to a dictionary.

Dictionary = {1: 1, 2: 4, 3: 9}

Dictionary['x'] = None 

print(Dictionary)


# In[15]:


#. Write a program to check if there is any numeric value in list using for loop.

thislist = ["apple", "banana", "cherry"]

for x in thislist:
    
  print(x)


# In[ ]:




