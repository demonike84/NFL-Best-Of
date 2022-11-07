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

#Pull Data from Spreadsheet
Receiving = pd.read_excel('assets/Receiving.xlsx', sheet_name = 'Receiving_Data')
#delete unused column
Receiving = Receiving.drop('Position', axis=1)
#Remove Players with less than 750 Yands in a year from list
Receiving2 = Receiving[Receiving['Receiving Yards'] > 750]
#Remove Players with less than 8 years in the leage
Receiving2 = Receiving2[Receiving2.groupby('Name')['Name'].transform('size')>8]
#Remove Duplicates
Receivers = [Receiving2['Name'].unique().tolist()]
#Create Master list of all players in case lookup is not in top list
AllReceivers = (Receiving['Name'].tolist())



# In[2]:

# In[3]:

#Create sorted list to veiw of TOP Players
df = pd.DataFrame(Receivers)
vals = df.T
vals.columns =["Top Player's"]
vals
sort = vals.sort_values(by=["Top Player's"])


# In[4]:

#Remove index from list and show list
buffer_list = sort.to_string(index=False).splitlines()
for line in buffer_list:
    print(line)

#Create Loop for bad entries

while True:
    Look = input("What Receiver are you wanting to look up:")
    if Look in AllReceivers:
        break
    else:
        print("Not in List, Try again")


# In[5]:

#Pull input from user to create charts
Receiver = Receiving[Receiving['Name'].str.contains(Look)]


# In[6]:

#Name Stats from excel sheet
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

#Plot Tables
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




