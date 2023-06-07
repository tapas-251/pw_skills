#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]'''

lst = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
lst.sort(key=lambda x: x[1])
print(lst)


# In[2]:


'''Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, lst))
print(squares)


# In[3]:


'''Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_of_strings = tuple(map(lambda x: str(x), lst))
print(tuple_of_strings)


# In[4]:


'''Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.'''

from functools import reduce

myList = range(1, 26)

product = reduce((lambda x, y: x * y), myList)

print(product)


# In[5]:


'''Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]'''

lst = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
result = list(filter(lambda x: (x % 2 == 0 and x % 3 == 0), lst))
print(result)


# In[6]:


'''Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']'''

lst = ['python', 'php', 'aba', 'radar', 'level']
result = list(filter(lambda x: (x == ''.join(reversed(x))), lst))
print(result)


# In[ ]:




