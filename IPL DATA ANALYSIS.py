#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#Seasons
Seasons = ["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"]
Sdict = {"2015":0,"2016":1,"2017":2,"2018":3,"2019":4,"2020":5,"2021":6,"2022":7,"2023":8,"2024":9}

#Players
Players = ["Sachin","Rahul","Smith","Sami","Pollard","Morris","Samson","Dhoni","Kohli","Sky"]
Pdict = {"Sachin":0,"Rahul":1,"Smith":2,"Sami":3,"Pollard":4,"Morris":5,"Samson":6,"Dhoni":7,"Kohli":8,"Sky":9}

#Salaries
Sachin_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
Rahul_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
Smith_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Sami_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
Pollard_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
Morris_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Samson_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
Dhoni_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
Kohli_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
Sky_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([Sachin_Salary, Rahul_Salary, Smith_Salary, Sami_Salary, Pollard_Salary, Morris_Salary, Samson_Salary, Dhoni_Salary, Kohli_Salary, Sky_Salary])

#Games
Sachin_G = [80,77,82,82,73,82,58,78,6,35]
Rahul_G = [82,57,82,79,76,72,60,72,79,80]
Smith_G = [79,78,75,81,76,79,62,76,77,69]
Sami_G = [80,65,77,66,69,77,55,67,77,40]
Pollard_G = [82,82,82,79,82,78,54,76,71,41]
Morris_G = [70,69,67,77,70,77,57,74,79,44]
Samson_G = [78,64,80,78,45,80,60,70,62,82]
Dhoni_G = [35,35,80,74,82,78,66,81,81,27]
Kohli_G = [40,40,40,81,78,81,39,0,10,51]
Sky_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([Sachin_G, Rahul_G, Smith_G, Sami_G, Pollard_G, Morris_G, Samson_G, Dhoni_G, Kohli_G, Sky_G])

#Points
Sachin_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
Rahul_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
Smith_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
Sami_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
Pollard_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
Morris_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
Samson_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
Dhoni_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
Kohli_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
Sky_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([Sachin_PTS, Rahul_PTS, Smith_PTS, Sami_PTS, Pollard_PTS, Morris_PTS, Samson_PTS, Dhoni_PTS, Kohli_PTS, Sky_PTS])


# In[2]:


Salary


# In[3]:


Games


# In[4]:


Points


# In[5]:


Games[5]


# In[6]:


Games[0:5]


# In[7]:


Games[0,5]


# In[8]:


Games[0,2]


# In[9]:


Games


# In[10]:


Games[1:2]


# In[11]:


Games


# In[12]:


Games[-3:-1]


# In[13]:


Games[-3,-1]


# In[14]:


Points


# In[15]:


Games


# In[16]:


Pdict


# In[17]:


Pdict['Sachin']


# In[18]:


Games[Pdict['Sachin']]


# In[19]:


Games


# In[20]:


Games[Pdict['Rahul']]


# In[21]:


Points


# In[22]:


Salary


# In[23]:


Games


# In[24]:


Salary/Games


# In[25]:


np.round(Salary/Games)


# In[26]:


import warnings
warnings.filterwarnings('ignore')


# In[ ]:





# In[27]:


import matplotlib.pyplot as plt


# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline #keep the plot inside jupyter nots instead of getting in other screen')


# In[ ]:


Salary


# In[ ]:


Salary[0]


# In[ ]:


plt.plot(Salary[0], color = 'black', ls = '--')


# In[ ]:


Games


# In[29]:


plt.plot(Salary[0], ls = '-.')


# In[30]:


plt.plot(Salary[1], color = 'purple', ls = '-')


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 7,3          # width,height


# In[32]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'o')


# In[33]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D')


# In[34]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 7,4


# In[35]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D', ms =5)     # ms = marker size


# In[36]:


list(range(10))


# In[37]:


Sdict


# In[38]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D', ms =5) 
plt.xticks(list(range(0,10)),Seasons)
plt.show()


# In[39]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D', ms =5) 
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
plt.show()


# In[40]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D', ms =5, label = Players[0]) 
plt.xticks(list(range(0,10)),Seasons, rotation = 'horizontal')
plt.show()


# In[41]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D', ms =5, label = Players[0]) 
plt.plot(Salary[1], color = 'purple', ls = '-', marker = 'o', ms =5, label = Players[1])
plt.show()


# In[42]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D', ms =5, label = Players[0]) 
plt.plot(Salary[1], color = 'purple', ls = '-', marker = 'o', ms =5, label = Players[1])
plt.plot(Salary[2], color = 'black', ls = '--', marker = 's', ms =5, label = Players[2]) 
plt.legend(loc = 'upper left', bbox_to_anchor=(0,0))
plt.show()


# In[43]:


plt.plot(Salary[0], color = 'blue', ls = ':', marker = 'D', ms =5, label = Players[0]) 
plt.plot(Salary[1], color = 'purple', ls = '-', marker = 'o', ms =5, label = Players[1])
plt.plot(Salary[2], color = 'black', ls = '--', marker = 's', ms =5, label = Players[2]) 
plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
plt.show()


# In[44]:


import matplotlib.pyplot as plt


# In[45]:


plt.plot(Points[0], color = 'RED', ls = '--')


# In[46]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[47]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Salary[3], c='Purple', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Salary[4], c='Black', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Salary[5], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Salary[6], c='Red', ls = '--', marker = '^', ms = 7, label = Players[6])
plt.plot(Salary[7], c='Red', ls = '--', marker = 'd', ms = 7, label = Players[7])
plt.plot(Salary[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
plt.plot(Salary[9], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[49]:


# we can visualize the how many games played by a player

plt.plot(Games[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Games[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Games[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Games[3], c='Red', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Games[4], c='Black', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Games[5], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Games[6], c='red', ls = '--', marker = '^', ms = 7, label = Players[6])
plt.plot(Games[7], c='Green', ls = '--', marker = 'd', ms = 7, label = Players[7])
plt.plot(Games[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
plt.plot(Games[9], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




