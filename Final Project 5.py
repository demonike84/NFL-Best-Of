#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install matplotlib
# pip install pandas
# pip install numpy
# pip install openpyxl
# pip install ipywidgets


# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


Receiving = pd.read_excel('assets/Receiving.xlsx', sheet_name = 'Receiving_Data')
Receiving = Receiving.drop('Position', axis=1)
#Receiving['Longest Reception'] = Receiving['Longest Reception'].str.replace(r'\W,"")

#print(Receiving)

Receiving2 = Receiving[Receiving['Receiving Yards'] > 750]
Receiving2 = Receiving2[Receiving2.groupby('Name')['Name'].transform('size')>8]
Receivers = [Receiving2['Name'].unique().tolist()]

# In[2]:


#Receiving2


# In[3]:


df = pd.DataFrame(Receivers)
vals = df.T
vals.columns =['Player']
vals
sort = vals.sort_values(by=['Player'])

#vals.sort_values(by=['Player'])
#print(sort)


# In[4]:

#print(sort.to_string(index=False))
buffer_list = sort.to_string(index=False).splitlines()
for line in buffer_list:
    print(line)

Look = input("What Receiver are you wanting to look up:")


# In[5]:


Receiver = Receiving[Receiving['Name'].str.contains(Look)]
#print(Receiver)


# In[6]:


Played = Receiver['Games Played']
Over40 = Receiver['Receptions Longer than 40 Yards']
Year = Receiver['Year']
First = Receiver['First Down Receptions']
YardsYear = Receiver['Receiving Yards']
GamesPlayed = Receiver['Games Played']
Rec = Receiver['Receptions']
Yr = Receiver['Year']
Lost = Receiver['Fumbles']


# In[7]:


plt.figure(figsize = (15, 6))
plt.bar(Yr, Over40)
plt.xlabel("Catches over 40 Yards")
plt.show()


# In[8]:


plt.figure(figsize = (15, 6))
plt.plot(Yr, YardsYear)
plt.xlabel("Receiving Yards per Year")
plt.show()


# In[9]:


plt.figure(figsize = (15, 6))
plt.bar(Yr, Lost)
plt.xlabel("Fumbles lost per Year")
plt.show()


# In[ ]:




