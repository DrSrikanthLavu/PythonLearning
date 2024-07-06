#!/usr/bin/env python
# coding: utf-8

# # 0. Useful functions

# In[ ]:


# to know type of an object/variable/item
type()


# In[ ]:


bool(), converts given value to a boolean value


# In[ ]:


id(), gives memory location of a variable


# # 1. Python Data types/ Data structures / data containter

# ## 1.1 Numbers

# - Integers
# - Floating point numbers
# - Complex numbers

# ### 1.1.1 Integers

# In[15]:


#variable declaration
# first student
a=60


# In[16]:


b=70


# In[17]:


c = a+b


# In[18]:


print(c)


# In[ ]:


#second student


# In[19]:


a = 68
b= 72


# In[ ]:


c= a+b
print(c)


# Here a, b and c are called variables, because their values can change.
# If the values doesn't change, they are called constants.

# ### 1.1.2 Floating point numbers

# In[22]:


# variable declaration- floating point numbers
d= 10.1
e= 23.45 
f = d+e
print(f)


# In[28]:


h = 10
j = 10.0
k = h+j


# In[25]:


type(h)


# In[29]:


type(j)


# In[30]:


type(k)


# In[31]:


h=10.0


# In[32]:


type(h)


# ## 1.2 boolean

# Has two values
# - True (any non zero)
# - False (0)

# In[34]:


x = True


# In[35]:


type(x)


# In[36]:


y= False


# In[37]:


type(y)


# In[38]:


z = bool(1)


# In[39]:


print(z)


# In[43]:


z1 = bool(-1)


# In[44]:


print(z1)


# In[45]:


z2= bool(0)
print(z2)


# ## 1.3 Mutability in Python

# In[ ]:


An object is mutable if we can change data it holds


# In[46]:


a = 10


# In[47]:


id(a)


# In[48]:


a = 20


# In[49]:


id(a)


# In[ ]:


Immutable


# ## 1.3.1 Immutable objects

# In[ ]:


- All numbers(integers, floats, complex numbers)
- Booleans
- strings
- tuples


# ## 1.3.2 Mutable objects

# In[ ]:


- Lists
- Dictionaries
- Sets


# In[78]:


a = True
print(a,id(a))


# ## 1.3.3 immutability implications

# In[80]:


b=a
print(b, id(b))


# In[81]:


a= False
print(a,id(a))


# In[82]:


print(b, id(b))


# ## 1.4 Python built-in constants

# In[ ]:


# built-in constants
- True
- False
- None


# In[51]:


A = True


# In[52]:


print(A)


# In[53]:


ab = 24
print(ab)


# In[54]:


B = False


# In[55]:


print(B)


# In[56]:


C = None


# In[57]:


print(C)


# In[58]:


type(C)


# In[59]:


type(A), type(B), type(C)


# ## 1.5 Variables in Python

# In[60]:


#typical variable declation
variable_name = value


# variable naming convention
# - 1.variable names are case sensitive
# - 2.variable name can not start with special character except '_'
# - 3.variable name can not start with number
# - 4.can not use reserved words/key words

# In[62]:


var1= 20


# In[63]:


print(var1)


# In[64]:


print(Var1)


# In[65]:


print(var1)


# In[66]:


print(vAr1)


# In[67]:


_var1 = 30
print(_var1)


# In[68]:


1var1 = 40


# In[69]:


true = 'USA'
print(true)


# In[70]:


True = 'USA'


# In[71]:


Var1 = 24


# In[72]:


print(Var1)


# In[ ]:


var1 


# In[73]:


x = True
x


# In[74]:


type(x)


# In[75]:


id(x)


# In[76]:


y= 'True'
print(y)


# In[77]:


type(y)


# ## 1.6 Python operators

# In[ ]:


# Addition: +
# Substraction : -
# Multiplication : *
# Division : /
# floored division(integer division): //
# modulus : % (gives you remainder)


# In[ ]:


2 + 5
# 2, 5 are called operands
# + is an operator


# In[83]:


5+2


# In[84]:


5-2


# In[85]:


5/3


# In[86]:


5//3


# In[87]:


5%3


# In[88]:


x = 'Srikanth'
x


# In[89]:


x*10


# In[90]:


x+2


# In[91]:


x= 'Srikanth'
y= 'lavu'
x+y


# ## 1.7 Python Conditional/comparison operators

# In[ ]:


# less than: <
# less than or equal to: <=
# equal to: ==
# greater than: >
# greater than or equal to: >=
# not equal to !=


# In[93]:


3 < 5


# In[94]:


x = 3 < 5


# In[95]:


x


# In[96]:


3 <= 5


# In[98]:


3 == 5


# In[99]:


x = 2


# In[102]:


y=3


# In[103]:


x == y


# In[104]:


x=y


# In[105]:


x


# In[106]:


y


# In[107]:


3 > 5


# In[108]:


4>=5


# In[109]:


3 != 5


# In[110]:


3==5


# In[111]:


1 == True


# In[116]:


5 == True


# In[117]:


bool(5) == True


# In[112]:


0 == False


# In[113]:


# This is strange, don't know why?
-1 == True


# In[118]:


bool(-1) == True


# In[114]:


# This is strange, don't know why?
-1 == False


# In[115]:


type(-1 == False)


# In[120]:


'A'  > 'a'


# In[121]:


'a' > 'A'


# In[122]:


'ca' < 'aa'


# In[123]:


'a' == 97
# don't know why?


# In[124]:


a == 10


# In[125]:


'*' > '+'


# ## 1.8 Python Logical operators

# In[ ]:


# and: returns first false value
# or: returns first true values
# not: flips boolean values of the operand


# In[126]:


# Boolean type has two values:
 - True (1 or non  zero)
 - False (0)


# In[127]:


False and True and True


# In[128]:


False and True and False


# In[129]:


True and True and True


# In[130]:


True and True and False


# In[131]:


False or True


# In[132]:


False or False


# In[133]:


5 and 0


# In[134]:


1 and 1


# In[135]:


1 and 0


# In[136]:


0 and 0


# In[137]:


1 or 0


# In[138]:


5 or 1


# In[139]:


-1 and 5


# In[140]:


0 or 0


# In[141]:


not 1


# In[142]:


not 0


# In[143]:


not 5


# In[144]:


not 'Srikanth'


# In[145]:


not -5


# In[146]:


True == 'True'


# In[ ]:




