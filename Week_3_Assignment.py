#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.'''

#To create a function in Python, you can use the keyword def. 

def odd_numbers():
    return [i for i in range(1, 26) if i % 2 != 0]
odd_numbers()

#This function will return a list of odd numbers from 1 to 25. 


# In[3]:


'''2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to
demonstrate their use.'''

#In Python, *args and **kwargs are used to pass a variable number of arguments to a function.

def my_function(*args):
    for arg in args:
        print(arg)

my_function('Hello', 'World', '!')

#This function will print out each argument passed to it.

#The **kwargs parameter is used to pass a variable number of keyword arguments to a function. Here is an example of a function that uses **kwargs:

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_function(first_name='Tapas', last_name='Das', age=37)

#This function will print out each keyword argument passed to it.


# In[5]:


'''Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,
18, 20].'''

# An iterator is an object that can be iterated (looped) upon. An object which will return data, one element at a time.
#To create an iterator in Python, one must implement the __iter__() and __next__() methods in the object. 
#The __iter__() method returns the iterator object itself. The __next__() method returns the next value from the iterator.

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iter = iter(my_list)

for i in range(5):
    print(next(my_iter))


# In[7]:


'''What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.'''

# A generator function is a special type of function that returns an iterator object with a sequence of values. 
# A generator function is defined like a normal function, but instead of using the return keyword to return a value, it uses the yield keyword.
# The yield keyword is used to produce a sequence of values that can be iterated over.
def my_generator():
    yield 100
    yield 200
    yield 300

for i in my_generator():
    print(i)


# In[8]:


'''Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers.'''

def prime_numbers():
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

prime_gen = prime_numbers()

for i in range(20):
    print(next(prime_gen))


# In[ ]:




