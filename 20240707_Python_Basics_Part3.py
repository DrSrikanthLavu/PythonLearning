#!/usr/bin/env python
# coding: utf-8

# ### Recapt of previous sessions

# In[ ]:


- introduction to Python.
- Python data types
    - numbers(integers/floats)
    - strings 
    - boolean( True/False)
    -complex number
    
- Mutability/immutability in Python

- Built-in constants
    - True
    - False
    - None

- Variable naming convention
- Python operators 
    - arithmetics operators( +, -, /, %, //)
    - Conditional operators( <, >, <=, >=, !=, ==)
    - logical operators ( and , or, not)
    
- reserved key words in pythons (35)
- Python expressions/ statements
- Order of operations(PEMDAS)
- How to read user entered input
- importance of variable naming and using appropirate comments in the program
- Conditional execution, if else, or if else if


# ## Exceptions handling in Python

# In[4]:


# calculate Body Mass Index of a person
# BMI = person weight in kgs/(height in meter)^2
weight_in_kgs = input("What is your weight in Kgs")

height_in_meters = input("What is your height in meters?")

Body_Mass_Index = float(weight_in_kgs)/float(height_in_meters)**2

print("Body Mass Index is ", Body_Mass_Index)


# In[2]:


print(x)


# In[3]:


type(x)


# In[5]:


weight_in_kgs = input("What is your weight in Kgs")

height_in_meters = input("What is your height in meters?")

Body_Mass_Index = float(weight_in_kgs)/float(height_in_meters)**2

print("Body Mass Index is ", Body_Mass_Index)


# In[ ]:


"try/ except"


# In[6]:


weight_in_kgs = input("What is your weight in Kgs")

height_in_meters = input("What is your height in meters?")

try:
    Body_Mass_Index = float(weight_in_kgs)/float(height_in_meters)**2
    print("Body Mass Index is ", Body_Mass_Index)
    
except:
    print('looks like Issue with user input of weight(kgs) and/or hieght(mtrs)')


# In[7]:


weight_in_kgs = input("What is your weight in Kgs")

height_in_meters = input("What is your height in meters?")

try:
    Body_Mass_Index = float(weight_in_kgs)/float(height_in_meters)**2
    print("Body Mass Index is ", Body_Mass_Index)
    
except:
    print('looks like Issue with user input of weight(kgs) and/or hieght(mtrs)')


# In[ ]:





# ## 3.8 Short-circuit of logical expressions

# In[9]:


x = 6
y = 0


# In[10]:


x >= 2 and (x/y) > 2


# In[11]:


x >= 10 and (x/y) > 2


# In[ ]:


(x >= 10) and ((x/y) > 2)


# ## Chapter 4

# ## Functions

# In[ ]:


a function is a named sequence of statements that performs a computation.
Every function has a name


# ## 4.2 Built-in functions

# In[ ]:


There are number of built-in functions.


# In[ ]:


print()


# In[12]:


name = 'Srikanth'
print(name)


# In[ ]:


max()


# In[13]:


max(10,-10, -20, 200)


# In[14]:


max(name)


# In[15]:


min(name)


# In[16]:


min(10,-10, -20, 200)


# In[17]:


len(name)


# In[18]:


len('Srikanth Lavu')


# In[19]:


len(10)


# In[ ]:


type()


# In[20]:


print(name)


# In[21]:


type(name)


# In[22]:


name=100.0
type(name)


# In[23]:


name=True
type(name)


# In[24]:


name=False
type(name)


# In[25]:


name=None
type(name)


# In[26]:


x= input("Enter your weight in Kgs ")


# In[27]:


print(x)


# In[28]:


type(x)


# In[29]:


y = float(x)
print(y)


# In[30]:


type(y)


# In[31]:


x1 = 10
print(x1)


# In[32]:


type(x1)


# In[33]:


y1='10'
print(y1)


# In[34]:


type(y1)


# In[35]:


y2 = int(y1)
type(y2)


# In[36]:


y3 = int('ABCD')


# In[37]:


help(int())


# In[38]:


help(print())


# In[ ]:


help()


# ## Math functions

# In[ ]:


"math" module


# In[39]:


import math


# In[40]:


print(math)


# In[41]:


help(math)


# ## 4.6 Custom functions

# In[ ]:


def name_of_your_function():
    statement1
    statement2
    .....
    statementN


# In[42]:


def BMI_Calculation(): 
    weight_in_kgs = input("What is your weight in Kgs")

    height_in_meters = input("What is your height in meters?")

    try:
        Body_Mass_Index = float(weight_in_kgs)/float(height_in_meters)**2
        print("Body Mass Index is ", Body_Mass_Index)
    
    except:
        print('looks like Issue with user input of weight(kgs) and/or hieght(mtrs)')


# In[43]:


BMI_Calculation()


# In[44]:


def product_of_two_numbers(x,y):
    print("the product of given numbers is: ", x*y)


# In[45]:


product_of_two_numbers(-10,10)


# In[46]:


def product_of_two_numbers_v2():
    number_1 = input("Enter first valid number:")
    number_2 = input("Enter second valid number:")
    print("the product of given numbers is: ", float(number_1)*float(number_2))


# In[47]:


product_of_two_numbers_v2()


# ## 4.10 Fruitful functions and void functions

# In[48]:


def product_of_two_numbers_v3():
    number_1 = input("Enter first valid number:")
    number_2 = input("Enter second valid number:")
    return float(number_1)*float(number_2)


# In[49]:


number_product_output = product_of_two_numbers_v3()


# In[50]:


print(number_product_output)


# In[51]:


number_product_output2 = product_of_two_numbers_v2()


# In[52]:


print(number_product_output2)


# In[ ]:




