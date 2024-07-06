#!/usr/bin/env python
# coding: utf-8

# ## Variable

# In[ ]:


A variable is a name that refers to a value.
As assignment statement creates new variables and gives them values.


# In[1]:


message = "this is samplw text message"
print(message)


# In[2]:


n=2024
print(n)


# In[3]:


#type
type(message)


# In[4]:


type(n)


# In[5]:


n2=10.54


# In[6]:


print(n2)


# In[7]:


type(n2)


# ## Python building blocks

# ### Variable names and keywords

# In[ ]:


Programmers generally choose names for their variables that are 
meaningful and document what the variable is used for.


# In[ ]:


variable naming convention
- 1.variable names are case sensitive
- 2.variable name can not start with special character except '_'
- 3.variable name can not start with number
- 4.can not use reserved words/key words


# In[12]:


MessagE1 = "sample test"
print(MessagE1)


# In[16]:


print(messagE1)


# In[17]:


_message2 = "Sample text 2"
print(_message2)


# In[18]:


3_message = "sample text 3"
print(3_message)


# Python has about 35 key words

# In[ ]:


False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield


# In[19]:


False = "Sample text 4"


# In[20]:


class = "7th Class"


# In[ ]:


# calculate body mass index BMI . BMI = weight in kgs/squre of (height in meter)


# In[27]:


#Programmer1 variable naming convention
x1 = 80
x2 = 1.8
x3 = x1/(x2*x2)


# In[28]:


print(x3)


# In[29]:


# programmer2 variable naming convention
weight_in_kgs = 80
height_in_meters = 1.8
Body_mass_index = weight_in_kgs/(height_in_meters*height_in_meters)
print(Body_mass_index)


# In[ ]:


#Programmer3 variable naming convention
x1 = 80  # give person weight in kgs
x2 = 1.8 # person height in meters
x3 = x1/(x2*x2) # calculate body mass Index(BMI) using formula weight in kgs/squre of (height in meter)


# Programmers should generally choose names for their variables that are meaningful and document what the variables are used for.

# ## Statements

# In[ ]:


A statement is a unit of code  thaat python interpreter can execute.


# In[ ]:


A script/program usually contains a sequence of statements.
If there is more than one statement, the results appear one at a 
time as the statements execute.


# In[31]:


x=2
print(x)
y=3
print(y)


# In[ ]:


two kinds of statements: 
    - print being an expression statement and 
    - assignment.


# ## Expressions

# In[ ]:


An expression is a combination of values, variables, and operators.


# In[ ]:


17
x=5
x+17


# ## Order of operations (PEMDAS)

# In[ ]:


When more than one operator appears in an expression, the order of 
evaluation depends on the rules of precedence.


# In[ ]:


PEMDAS: Parenthesis, Exponential, Multiplication, Division, addition, subtraction


# In[ ]:


1. Parentheses have the highest precedence
2. Exponentiation has the next highest precedence
3. Multiplication and Division have the same precedence, which is higher
than Addition and Subtraction
4. Operators with the same precedence are evaluated from left to right

Tip: When in doubt, always put parentheses in your expressions to 
make sure the com- putations are performed in the order you intend.


# In[ ]:


x = 2*(4*6*(3*2))

-> 2*(4*6*6)
->2*(144)
-> 288


# In[32]:


x1 = 2**3 # this is two cube
print(x1)


# In[33]:


x2 = 3*1**3
print(x2)


# In[34]:


x3 = 2*3-1
print(x3)


# In[35]:


x4 = (2*3)-1
print(x4)


# In[37]:


x5 = 6+4/2
print(x5)


# In[38]:


x6 = 6+(4/2)
print(x6)


# In[39]:


#Operators with the same precedence are evaluated from left to right.
x7 = 5-3-1 # 1 or 3
print(x7)


# In[40]:


x8 = (5-3)-1
print(x8)


# ## String Operations

# In[41]:


print(x8)


# In[42]:


print('x8')


# In[ ]:


The + operator works with strings, but it is not addition in 
the mathematical sense. Instead it performs concatenation,
which means joining the strings by linking them end to end.


# In[44]:


first = 10
second = 15
print(first+second)


# In[45]:


first = '10'
second = '15'
print(first+second)


# In[47]:


first_name = 'Srikanth'
second_name = 'Lavu'
print(first_name+' '+second_name)


# In[48]:


print(first_name*3)


# ## Asking the user for input

# In[49]:


variable_name = input()


# In[50]:


print(variable_name)


# In[51]:


name = input('What is your name?')


# In[52]:


print(name)


# In[53]:


name = input('What is your name? \n')


# In[54]:


print(name)


# In[55]:


weight_in_kgs = input('What is your weight in Kgs? \n')
height_in_meters = input('What is your height in meters? \n')
Body_Mass_Index = float(weight_in_kgs)/float(height_in_meters)**2
print("Body Mass Index is ", Body_Mass_Index)


# In[56]:


print("Body Mass Index is ", Body_Mass_Index)


# In[57]:


type(weight_in_kgs)


# ## Comments

# In[ ]:


As programs get bigger and more complicated, they get more difficult
to read.
For this reason, it is a good idea to add notes to your programs to 
explain in natural language what the program is doing.
These notes are called comments, and in Python they start with the 
# symbol:


# # Chapter 3 Conditional Execution

# ## Boolean expression

# In[ ]:


A boolean expression is an expression that is either true or false.


# In[60]:


5 == 5


# In[61]:


5 == 6


# In[ ]:


True and False are special values that belong to the class bool; 
they are not strings


# In[62]:


type(True)


# In[63]:


type(False)


# In[ ]:


The == operator is one of the comparison operators;
the others are:
x!=y   #x is not equaltoy
x>y    # x is greater than y
x<y    #x is less than y
x>=y   # x is greater than or equal to y 
x<=y   #xis less than or equal to y 
x is y  #x is the same as y
x is not y # x is not the same as y

the Python symbols are different from the mathematical symbols 
for the same operations.


# ## 3.2 Logical Operators

# In[ ]:


There are three logical operators: and, or, and not.


# In[64]:


x = 5


# In[65]:


x > 0 and x<10


# In[66]:


# if the number is divisible by 2 or 3.
x%2 == 0 or x%3 == 0


# In[67]:


x=12
x%2 == 0 or x%3 == 0


# ## 3.3 Conditional execution

# In[ ]:


execute if the condition is met/true


# In[ ]:


we almost always need the ability to check conditions 
and change the behavior of the program accordingly.


# In[ ]:


#format of conditional execution in python
if your_expression:
    list of statements


# In[69]:


if x > 0 :
    print('x is positive')


# In[70]:


x = 0
if x > 0 :
    print('x is positive')


# In[72]:


age = -20
if age < 0:
    pass


# In[71]:


age = -1
if age < 0:
    print(" Enter some positive meaningful age!")


# ## 3.4 Alternative execution

# In[73]:


# write a program to print whether the input number is even or odd


# In[74]:


#ask user to enter a positive integer
number = input("Enter a positive integer \n")
if (number%2 == 0):
    print("Gicven number is even")
else :
    print("Given number is odd")


# In[75]:


type(number)


# In[76]:


#ask user to enter a positive integer
number = input("Enter a positive integer \n")
if (int(number)%2 == 0):
    print("Given number is even")
else :
    print("Given number is odd")


# ## 3.5 Chained Conditionals

# In[ ]:


# take two numbers x and y and print whether 
- x is less than y
- x is greater than y
- x is equal to y


# In[77]:


# input x value
x = input("enter x value \n")
y = input("enter y value \n")

x1 = float(x) #covert x into number
y1 = float(y) #covert y into number

#logic to compare and x and y
if x1 == y1:
    print(" x and y are equal")
else:
    print(" x and y are not equal")


# In[78]:


#logic to compare and x and y
x = input("enter x value \n")
y = input("enter y value \n")

x1 = float(x) #covert x into number
y1 = float(y) #covert y into number
if x1 == y1:
    print(" x and y are equal")
elif x1 > y1:
    print(" x is greater than y")
else:
    print("x is less than y")


# ## 3.6 Nested Conditionals

# In[ ]:


One conditional can also be nested within another.


# In[79]:


#logic to compare and x and y
x = input("enter x value \n")
y = input("enter y value \n")

x1 = float(x) #covert x into number
y1 = float(y) #covert y into number
if x1 == y1:
    print(" x and y are equal")
else:
    if x1 > y1:
        print(" x is greater than y")
    else:
        print("x is less than y")


# ## 3.7 Catching exceptions using try and except

# In[ ]:


will discuss in next session


# ## 3.8

# In[ ]:




