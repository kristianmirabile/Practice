#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a > b:
            return b
        else:
            return a
    elif a%2 != 0 or b%2 != 0:
        if a > b:
            return a
        else:
            return b


# In[162]:


lesser_of_two_evens(2,4)


# In[3]:


lesser_of_two_evens(2,5)


# In[85]:


def animal_crackers(text):
    x = text.split()
    first = x[0][0]
    second = x[1][0]
    if first == second:
        return True
    else:
        return False


animal_crackers('llamma llamma')
    


# In[86]:


print(animal_crackers('lumbering llammas'))


# In[87]:


animal_crackers('loopy whales')


# In[88]:


def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1+n2 == 20:
        return True
    else:
        return False


# In[89]:


makes_twenty(1, 20)


# In[90]:


makes_twenty(5, 15)


# In[91]:


makes_twenty(5, 5)


# In[139]:


def old_macdonald(name):
    firsthalf = name[:3]
    secondhalf = name[3:]
    print(firsthalf.capitalize()+secondhalf.capitalize())


# In[142]:


old_macdonald('macdonald')


# In[145]:


def master_yoda(text):
    stringed = text.split()
    reverse = stringed[::-1]
    yoda = " ".join(reverse)
    print(yoda)


# In[163]:


master_yoda('we are here')


# In[153]:


def almost_there(n):
    x = range(90, 110)
    y = range(190, 210)
    
    if n in x:
        return True
    elif n in y:
        return True
    else:
        return False


# In[154]:


almost_there(92)


# In[155]:


almost_there(150)


# In[156]:


almost_there(209)


# In[ ]:




