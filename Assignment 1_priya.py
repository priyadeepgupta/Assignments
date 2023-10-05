#!/usr/bin/env python
# coding: utf-8

#             ASSIGNMENT 1
#            

# In[20]:


# 1. write a python program to replace all occurences of space, dot or comma with a colon.

import re

sample_text = 'Python Exercies, PHP Exercises'
x = re.sub('[.,\s]', ':',sample_text)
print(x)


# In[ ]:





# In[ ]:


# 2. Write a python program to find all words starting with 'a or 'e' in a given string.



# In[25]:


import re

string = "Apples, Bananas and Grapes are Fruits but eagle is a bird"
pattern = r'\b[aeAE]\w+\b'
result = re.findall(pattern, string)
print(result)


# In[ ]:





# In[39]:


# 3. create a function in python to find all words that are at least  4 characters long in a string. The use of re.compile()is compulsory.

import re

string = "There are only apples, bananas, grapes and oranges are available in the market"
pattern = re.compile(r'\b\w{4,}\b')
words4char = pattern.findall(string)
print(words4char)


# In[ ]:





# In[ ]:




