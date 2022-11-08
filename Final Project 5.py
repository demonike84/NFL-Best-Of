#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install matplotlib
# pip install pandas



# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


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


print(Receiving.dtypes)
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
Choice = Receiving[Receiving['Name'].str.contains(Look)]
Best = Receiving[Receiving['Name'].str.contains('Rice, Jerry')]


# In[6]:

#Choice Stats from excel sheet
Played = Choice['Games Played']
Over40 = Choice['Receptions Longer than 40 Yards']
Year = Choice['Year']
First = Choice['First Down Receptions']
YardsYear = Choice['Receiving Yards']
GamesPlayed = Choice['Games Played']
Rec = Choice['Receptions']
Yr = Choice['Year']
Lost = Choice['Fumbles']

#Choice Stats from excel sheet
BPlayed = Best['Games Played']
BOver40 = Best['Receptions Longer than 40 Yards']
BYear = Best['Year']
BFirst = Best['First Down Receptions']
BYardsYear = Best['Receiving Yards']
BGamesPlayed = Best['Games Played']
BRec = Best['Receptions']
BYr = Best['Year']
BLost = Best['Fumbles']


# In[7]:

#Plot Tables
#plt.figure(figsize = (15, 6))
#plt.bar(Yr, Over40)
#plt.xlabel("Catches over 40 Yards")
#plt.show()


# In[8]:


fig, axis = plt.subplots(2,2)
fig.suptitle("Who's the Best?")

#plt.figure(figsize = (15, 6))

axis[0, 0].plot(BYr, BYardsYear)
axis[0, 0].set_title("Jerry Rice")

axis[0, 1].plot(Yr, YardsYear)
axis[0, 1].set_title(Look)

axis[1, 0].plot(BYr, BOver40)
#axis[1, 0].set_title("Catches over 40 Yards")

axis[1, 1].plot(Yr, Over40)
#axis[1, 1].set_title("Cosine Function")



#plt.subplot(1, 1)
#plt.subplot(BYr, BYardsYear)

#plt.subplot(2, 2)
#plt.subplot(Yr, YardsYear)

plt.xlabel("Receiving Yards per Year")
plt.show()


# In[9]:


plt.figure(figsize = (15, 6))
plt.bar(Yr, Lost)
plt.xlabel("Fumbles lost per Year")
#plt.show()


# In[ ]:


print("Have a good day!")
