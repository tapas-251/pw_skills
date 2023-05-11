#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1. Create one variable containing following type of data:

#(i)	string
a = ("pwskills")
print(type(a))
#(ii)	list
b = ["apple","papaya","strawberry"]
print(type(b))
#(iii)	float
c = 206.754
print(type(c))
#(iv)	tuple
tuple1 = (3, 4.6, "dog")
print(type(tuple1))


# In[3]:


#Q2. Given are some following variables containing data:

#(i)	var1 = ‘ ‘
#var1 = ‘ ‘
#print(type(var1))
# data type is invalid character

#(ii)	var2 = ‘[ DS , ML , Python]’
var2 = "[ DS , ML , Python]"
print(type(var2))
# data type is String

#(iii)	var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
var3 = [ "DS" , "ML" , "Python"]
print(type(var3))
# data type is list

#(iv)	var4 = 1.
var4 = 1.
print(type(var4))
# data type is float


# In[4]:


#Q3. Explain the use of the following operators using an example:

#(i)	/
a = 10
b = 2
c = a/b
print(c)
# / is a division operator

#(ii)	%
d = 24
e = 7
f = d % e
print(f)
# % is the modulus operator which shows the remainder of the division of the variables

#(iii)	//

aa = 30
bb = 15
cc = aa // bb
print(cc)
# // is the floor division operator which rounds the division result down to the nearest whole number

#(iv)	**
dd = 10
ee = 3
ff = dd ** ee
print(ff)
# ** is the to the power operator whcih returns first raised to power second


# In[6]:


"""Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type."""

choice = [1,2.0,5,"example",(1,2),"1x","test",("ace"),25,47]
for item in choice:
    print (item, " is ", type(item))


# In[7]:


"""Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible."""

A = 232
B = 4
division_count = 0
while A % B == 0:
    division_count += 1
    A /= B
print("A is divisible by B", division_count, "times")


# In[8]:


"""Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not"""

my_list = [item for item in range(25)]
for item in my_list:
    if item % 3 == 0:
        print(item, "is divisible by 3")
    else:
        print(item, "is not divisible by 3")


# Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property
# 
# If the state of an object in a given list can be modified anytime after it is created then it is known as Mutable object.
#  For example, objects in a list can be modified which makes it mutable. Please check the below code where in we have
#  modified an object in the list.
#  
# my_list = [1, 2, 3]
# print(my_list)
# my_list[0] = 'a new value'
# print(my_list)
# 
# Immutable data types are the ojects which cannot be modified after it is created. Tuples, object id or dictionary keys are
#  examples of immutable data types.
# 

# In[ ]:




