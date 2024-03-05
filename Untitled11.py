#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


file_path = r"C:\Users\majji\Downloads\SportsKPI_Kabaddi_Dataset_for_Assessment.xlsx"
data = pd.read_excel(file_path)


# In[4]:


data


# In[5]:


raiding_total_raids = data.shape[0]
raiding_successful_raids = data[data['Outcome'] == 'Successful' ].shape[0]


# In[6]:


print("Overall Raiding Team’s Total Raids:", raiding_total_raids)
print("Overall Raiding Team’s Successful Raids:", raiding_successful_raids)


# In[33]:


raiding_total_raids=data.groupby('Raiding_Team_Name').size()
raiding_successful_raids=data[data['Outcome']=='Successful'].groupby('Raiding_Team_Name').size()
print("Overall Raiding Team’s Total Raids:", raiding_total_raids)
print("Overall Raiding Team’s Successful Raids:", raiding_successful_raids)


# In[7]:


defending_total_tackles = data[(data['Outcome'] == 'Successful') | (data['Outcome'] == 'Unsuccessful')].shape[0]
defending_successful_tackles = data[(data['Outcome'] == 'Unsuccessful')].shape[0]


# In[8]:


print("Overall Defending Team’s Total Tackles:", defending_total_tackles)
print("Overall Defending Team’s Successful Tackles:", defending_successful_tackles)


# In[36]:


defending_total_tackles = data[(data['Outcome'] == 'Successful') | (data['Outcome'] == 'Unsuccessful')].groupby('Defending_Team_Name').size()
defending_successful_tackles = data[(data['Outcome'] == 'Unsuccessful')].groupby('Defending_Team_Name').size()


# In[37]:


print("Overall Defending Team’s Total Tackles:", defending_total_tackles)
print("Overall Defending Team’s Successful Tackles:", defending_successful_tackles)


# In[9]:


raiding_successful_raids_6_7_def_teams = data[(data['Outcome'] == 'Successful') & ((data['Number_of_Defenders'] == 6) | (data['Number_of_Defenders'] == 7))]['Raiding_Team_Name'].unique()


# In[10]:


# Display the unique raiding team names
print("Raiding Team’s Successful Raids against 6-7 Defenders ONLY:")
for team in raiding_successful_raids_6_7_def_teams:
    print(team)


# In[11]:


Defending_Team_Successful_Tackles_against_1_2_3_Defenders= data[(data['Outcome']=='Unsuccessful') & ((data['Number_of_Defenders']==1)|(data['Number_of_Defenders']==2)|(data['Number_of_Defenders']==3))]['Defending_Team_Name'].unique()


# In[12]:


print("Defending_Team_Successful_Tackles_against_1_2_3_Defenders:")
for team in Defending_Team_Successful_Tackles_against_1_2_3_Defenders:
    print(team)


# In[13]:


grouped_data = data[data['Raid_Number'] == 3].groupby('Raiding_Team_Name')


# In[14]:


team_success_ratios = {}


# In[15]:


for team, group in grouped_data:
    # Count total number of Do_or_Die Raids for the team
    total_do_or_die_raids_team = group.shape[0]
    
    succ_do_or_die_raids_team = group[group['Outcome'] == 'Successful'].shape[0]
    
    success_ratio = succ_do_or_die_raids_team / total_do_or_die_raids_team if total_do_or_die_raids_team != 0 else 0
    
    team_success_ratios[team] = success_ratio


# In[16]:


print("Success Ratios of Do_or_Die Raids for Each Raiding Team:")
for team, ratio in team_success_ratios.items():
    print(f"{team}: {ratio}")


# In[17]:


raider_success_counts=data[(data['Outcome']=='Successful')]['Raider_Name'].value_counts()
most_successful_raider = raider_success_counts.idxmax()
print("Most Successful Raider:", most_successful_raider)


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


raider_name = 'HIMANSHU'  # Replace 'Raider_X' with actual raider's name
raids_distribution = data[data['Raider_Name'] == raider_name]['Outcome'].value_counts()
plt.figure(figsize=(8, 6))
raids_distribution.plot(kind='bar', color=['green', 'yellow','red'])
plt.title('Distribution of Raids for ' + raider_name)
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()


# In[20]:


do_or_die_raider_count=data[(data['Outcome']=='Successful') & (data['Raid_Number']==3)]['Raider_Name'].value_counts()
sucessful_do_or_die_raider=do_or_die_raider_count.idxmax()


# In[21]:


print("Most Successful do or die Raider :",sucessful_do_or_die_raider)


# In[22]:


defender_success_counts=data[(data['Counter_Action_Skill']=='Struggle')][['Defender_1_Name', 'Defender_2_Name']].value_counts()
Most_successful_defender= defender_success_counts.idxmax()
print("Most Successful Raider:", Most_successful_defender)


# In[27]:


# Distribution of Tackles for a Defender
defender_name = 'SUMIT'  # Replace 'Defender_Y' with actual defender's name
data['Outcome'] = data['Outcome'].map({'Successful': 'Unsuccessful', 'Unsuccessful': 'Successful'})
tackles_distribution = data[data[['Defender_1_Name', 'Defender_2_Name']].isin([defender_name]).any(axis=1)]['Outcome'].value_counts()
plt.figure(figsize=(8, 6))
tackles_distribution.plot(kind='bar', color=['green', 'red'])
plt.title('Distribution of Tackles for ' + defender_name)
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()


# In[30]:


import matplotlib.pyplot as plt

raider_name = 'HIMANSHU'  # Replace 'HIMANSHU' with the actual raider's name

# Filter the data for the specified raider and non-empty attacking skills
raider_data = data[(data['Raider_Name'] == raider_name) & (data['Attacking_Skill'].notnull()) & (data['Attacking_Skill'] != ' ')]

# Calculate the distribution of attacking skills for the raider
attacking_skills_distribution = raider_data['Attacking_Skill'].value_counts()

# Plot the distribution
plt.figure(figsize=(10, 6))
attacking_skills_distribution.plot(kind='bar', color='blue')
plt.title('Attacking Skills Distribution for ' + raider_name)
plt.xlabel('Attacking Skill')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[32]:


defender_name = 'SUMIT'  # Replace 'SUMIT' with the actual defender's name

# Filter the data for the specified defender and non-null defensive skills
defender_data = data[((data['Defender_1_Name'] == defender_name) | (data['Defender_2_Name'] == defender_name)) & 
                     (data['Defensive_Skill'].notnull()) & (data['Defensive_Skill'] != ' ')]

# Calculate the distribution of defensive skills for the defender
defensive_skills_distribution = defender_data['Defensive_Skill'].value_counts()

# Plot the distribution
plt.figure(figsize=(10, 6))
defensive_skills_distribution.plot(kind='bar', color='green')
plt.title('Defensive Skills Distribution for ' + defender_name)
plt.xlabel('Defensive Skill')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




