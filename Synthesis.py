#!/usr/bin/env python
# coding: utf-8

# In[61]:


import IPython.display as ipd


# In[62]:


import sounddevice as sd
import numpy as np


# In[63]:


def pianoNote(frequency):
    pi = np.pi
    time = np.linspace(0, 1, num= 44100)
    Y = np.sin(2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time)
    
    # Adding overnotes 
    
    Y += np.sin(2 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 2
    Y += np.sin(3 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 4
    Y += np.sin(4 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 8
    Y += np.sin(5 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 16
    Y += np.sin(6 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 32
    
    Y += Y * Y * Y
    
    Y *= 1 + 16 * time * np.exp(-6 * time)
    
    return Y


# In[64]:


# key = pianoNote(7902.133)


# In[65]:


def keyFreq(n):
    return 440*((np.power(2, 1./12))**(n-49))


# In[100]:


key = pianoNote(keyFreq(40))


# In[101]:


ipd.Audio(key, rate=44100)


# In[ ]:


x = np.linspace(0, 1, num=44100)
w = np.sin(2)

