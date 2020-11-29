#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyshorteners


# In[2]:


def shortener(link):
    short = pyshorteners.Shortener()
    short_link = short.tinyurl.short(link)
    return short_link


# In[4]:


url = input("Enter url:")
final = shortener(url)
print(f"Shortened link is {final}")


# In[ ]:




