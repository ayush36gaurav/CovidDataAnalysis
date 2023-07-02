# import pandas for working on dataframe
import pandas as pd
# Import matplotlib for plotting
import matplotlib.pyplot as plt


# Part A
# Annotate the output screen that part A begins here
print('Part A')
# Make a variable to store the population of Delhi
pop_delhi = 20591874

# Read the .csv file
df = pd.read_csv('Cowin_Vaccine_Data_Districtwise.csv',low_memory=False)

# Extract only those rows which contain the data for Delhi in new dataframe
df_delhi_regions = df.loc[df[df['State']=='Delhi'].index]
# Delete unwanted columns from the dataset and make new dataframe
ndf_delhi_regions = df_delhi_regions.drop(['S No','State_Code','State','District_Key','Cowin Key','District'],axis=1)
# transpose the dataset to be able to work on dates
trans_df_delhi = ndf_delhi_regions.transpose()
# Convert the data type of the rows having numbers as strings
trans_df_delhi[[146,147,148,149,150,151,152,153,154,155,156]] = trans_df_delhi[[146,147,148,149,150,151,152,153,154,155,156]].apply(pd.to_numeric)
# Add the data for all sub-regions of Delhi and get data for entire Delhi in new column
trans_df_delhi['Delhi'] = trans_df_delhi[146] + trans_df_delhi[147] + trans_df_delhi[148] + trans_df_delhi[149] + trans_df_delhi[150] + trans_df_delhi[151] + trans_df_delhi[152] + trans_df_delhi[153] + trans_df_delhi[154] + trans_df_delhi[155] + trans_df_delhi[156]
# Delete the data of sub-regions now and make another dataframe
only_delhi = trans_df_delhi.drop([146,147,148,149,150,151,152,153,154,155,156],axis=1)
# Make a new dataframe and store all the labels in it
labels =  df.loc[0]
# Delete unwanted labels and keep only dates in it
only_labels = labels.drop(['S No','State_Code','State','District_Key','Cowin Key','District'])
# Make a new dataframe having data for Delhi with labels of dates
df_delhi_with_labels = only_delhi.join(only_labels)

# Make a new datframe and extract data only for First Dose only in it
df_delhi_firstdose = df_delhi_with_labels.loc[df_delhi_with_labels[df_delhi_with_labels[0]=='First Dose Administered'].index]
# Make a separate column and store the vaccination coverage of first dose in it
df_delhi_firstdose['Vaccination Coverage'] = (df_delhi_firstdose['Delhi']*100)/pop_delhi
# Make a new datframe and extract data only for Second Dose only in it
df_delhi_seconddose = df_delhi_with_labels.loc[df_delhi_with_labels[df_delhi_with_labels[0]=='Second Dose Administered'].index]
# Make a separate column and store the vaccination coverage of second dose in it
df_delhi_seconddose['Vaccination Coverage'] = (df_delhi_seconddose['Delhi']*100)/pop_delhi

# Keep the dates in a separate variable for plotting on x-axes
dates = df_delhi_seconddose.index
# Store the ticks to be made on x-axes in a list
tick = ['16-01-2021.4','16-02-2021.4','16-03-2021.4','16-04-2021.4','16-05-2021.4','16-06-2021.4','16-07-2021.4','16-08-2021.4','16-09-2021.4','16-10-2021.4']
# Store the labels for these ticks in a separate list
label = ['16th\nJan 2021','16th\nFeb','16th\nMar','16th\nApr','16th\nMay','16th\nJune','16th\nJuly','16th\nAug','16th\nSep','16th\nOct']

# Plot the vaccinntion coverage for first and second dose in Delhi
plt.plot(dates,df_delhi_firstdose['Vaccination Coverage'])
plt.plot(dates,df_delhi_seconddose['Vaccination Coverage'])
# Give legend, ticks, label, tiltle and limits to axes
plt.legend(['First Dose','Second Dose'])
plt.ylim(top=100)
plt.xticks(ticks=tick,labels=label)
plt.xlabel('Time in Month')
plt.ylabel('%age Coverage')
plt.title('Vaccination Coverage for Delhi')
# Display the grid and show the plot
plt.grid()
plt.show()

# Make a variable to store the population of Mumbai
pop_mumbai = 20667656

# Extract the row which contains the data for Mumbai in new dataframe
df_mumbai = df.loc[df[df['District']=='Mumbai'].index]
# Delete unwanted columns from the dataset and make new dataframe
ndf_mumbai = df_mumbai.drop(['S No','State_Code','State','District_Key','Cowin Key','District'],axis=1)
# transpose the dataset to be able to work on dates
trans_df_mumbai = ndf_mumbai.transpose()
# Convert the data type of the rows having numbers as strings
trans_df_mumbai[393] = trans_df_mumbai[393].apply(pd.to_numeric)
# Make a new dataframe having data for Mumbai with labels of dates
df_mumbai_with_labels = trans_df_mumbai.join(only_labels)

# Make a new datframe and extract data only for First Dose only in it
df_mumbai_firstdose = df_mumbai_with_labels.loc[df_mumbai_with_labels[df_mumbai_with_labels[0]=='First Dose Administered'].index]
# Make a separate column and store the vaccination coverage of first dose in it
df_mumbai_firstdose['Vaccination Coverage'] = (df_mumbai_firstdose[393]*100)/pop_mumbai
# Make a new datframe and extract data only for Second Dose only in it
df_mumbai_seconddose = df_mumbai_with_labels.loc[df_mumbai_with_labels[df_mumbai_with_labels[0]=='Second Dose Administered'].index]
# Make a separate column and store the vaccination coverage of second dose in it
df_mumbai_seconddose['Vaccination Coverage'] = (df_mumbai_seconddose[393]*100)/pop_mumbai

# Plot the vaccinntion coverage for first and second dose in Mumbai
plt.plot(dates,df_mumbai_firstdose['Vaccination Coverage'])
plt.plot(dates,df_mumbai_seconddose['Vaccination Coverage'])
# Give legend, ticks, label, tiltle and limits to axes
plt.legend(['First Dose','Second Dose'])
plt.ylim(top=100)
plt.xticks(ticks=tick,labels=label)
plt.xlabel('Time in Month')
plt.ylabel('%age Coverage')
plt.title('Vaccination Coverage for Mumbai')
# Display the grid and show the plot
plt.grid()
plt.show()

# Leave a blank line
print()


# Part B
# Annotate the output screen that part B begins here
print('Part B')

# Make variables and store the area of Delhi and Mumbai
area_delhi = 1400
area_mumbai = 670

# Generate a list of numbers to make it as index of dataframes
numbers = [x for x in range(289)]

# Make a new datframe and extract data for sites in Delhi only in it
df_delhi_sites = df_delhi_with_labels.loc[df_delhi_with_labels[df_delhi_with_labels[0]=='Sites '].index]
# Make a new column and store sites per unit area for each date in it
df_delhi_sites['Sites/area'] = df_delhi_sites['Delhi']/area_delhi
# Make a new datframe and extract data for sessions in Delhi only in it
df_delhi_sessions = df_delhi_with_labels.loc[df_delhi_with_labels[df_delhi_with_labels[0]=='Sessions'].index]
# Make a new column and store sesssions per unit area for each date in it
df_delhi_sessions['Sessions/area'] = df_delhi_sessions['Delhi']/area_delhi
# Make a new datframe and extract data for sites in Mumbai only in it
df_mumbai_sites = df_mumbai_with_labels.loc[df_mumbai_with_labels[df_mumbai_with_labels[0]=='Sites '].index]
# Make a new column and store sites per unit area for each date in it
df_mumbai_sites['Sites/area'] = df_mumbai_sites[393]/area_mumbai
# Make a new datframe and extract data for sessions in Mumbai only in it
df_mumbai_sessions = df_mumbai_with_labels.loc[df_mumbai_with_labels[df_mumbai_with_labels[0]=='Sessions'].index]
# Make a new column and store sessions per unit area for each date in it
df_mumbai_sessions['Sessions/area'] = df_mumbai_sessions[393]/area_mumbai

# In each dataframe for first dose coverage, sites and sessions in Delhi and Mumbai, add another column having index values
df_delhi_sites['Index'] = numbers
df_delhi_sessions['Index'] = numbers
df_delhi_firstdose['Index'] = numbers
df_mumbai_sites['Index'] = numbers
df_mumbai_sessions['Index'] = numbers
df_mumbai_firstdose['Index'] = numbers

# Reset the index of each of the above dataframes to the value of the column containing indexes
df_delhi_sites.reset_index(inplace=True)
df_delhi_sessions.reset_index(inplace=True)
df_delhi_firstdose.reset_index(inplace=True)
df_mumbai_sites.reset_index(inplace=True)
df_mumbai_sessions.reset_index(inplace=True)
df_mumbai_firstdose.reset_index(inplace=True)

# Find the value of correlation, round ir to four places of decimal
# And print the value on the screen
print('The correlation of First Dose Coverage with sites per unit area for Delhi is ' + str(round(df_delhi_firstdose['Vaccination Coverage'].corr(df_delhi_sites['Sites/area']),4)) + '.')
print('The correlation of First Dose Coverage with sessions per unit area for Delhi is ' + str(round(df_delhi_firstdose['Vaccination Coverage'].corr(df_delhi_sessions['Sessions/area']),4)) + '.')
print('The correlation of First Dose Coverage with sites per unit area for Mumbai is ' + str(round(df_mumbai_firstdose['Vaccination Coverage'].corr(df_mumbai_sites['Sites/area']),4)) + '.')
print('The correlation of First Dose Coverage with sessions per unit area for Mumbai is ' + str(round(df_mumbai_firstdose['Vaccination Coverage'].corr(df_mumbai_sessions['Sessions/area']),4)) + '.')

# Leave a blank line
print()


# Part C
# Annotate the output screen that part C begins here
print('Part C')

# Delete the row containing labels of sessions, sites etc.
df = df.drop(index=0)

# Change the data type of the column containing total number of First Doses given to integer
df['31-10-2021.3'] = df['31-10-2021.3'].apply(pd.to_numeric)
# Group the data for the districts of a state and add their value to get the data for each state
grouped_df = df.groupby('State').sum()

# Generate a list of numbers to make it as index of the grouped dataframe
number = [x for x in range(36)]
# Add another column storing index values to the grouped dataframe
grouped_df['Index'] = number
# Reset the index of the grouped dataframe to the value of the column storing indexes
grouped_df.reset_index(inplace=True)

# Find the value of highest vaccination done in a state
highest_vaccination = max(grouped_df['31-10-2021.3'])
# Find the index of the row storing data for highest vaccination
index_highest_vaccination = grouped_df[grouped_df['31-10-2021.3'] == highest_vaccination].index.values
# Extract the name of the state from the index and print the name on the screen
print('The state/UT having highest vaccination is ' + str(grouped_df.at[int(index_highest_vaccination),'State']) + '.')
