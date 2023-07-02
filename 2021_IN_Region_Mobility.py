# Import Pandas for working on the dataframe
import pandas as pd
# Import matplotlib for plotting
import matplotlib.pyplot as plt
# Import datetime for working with datetime values
from datetime import datetime


# Part A
# Annotate the output screen that part A begins here
print('Part A')

# Read the .csv with only specific columns
df = pd.read_csv('2021_IN_Region_Mobility_Report.csv',usecols=['sub_region_1','sub_region_2','date','retail_and_recreation_percent_change_from_baseline','transit_stations_percent_change_from_baseline'])

# Change the data type of the Date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Find indexes in the data drame which contain the data for Delhi and Mumbai
index_nos_delhi = df[df['sub_region_1'] == 'Delhi'].index
index_nos_mumbai1 = df[df['sub_region_2'] == 'Mumbai'].index
index_nos_mumbai_suburban = df[df['sub_region_2'] == 'Mumbai Suburban'].index

# Since two set of indexes contain data for Mumbai, merge them
index_nos_mumbai = index_nos_mumbai1.union(index_nos_mumbai_suburban)

# Make separate dataframe for each of Delhi and Mumbai using the indexes found above
df_delhi = df.loc[index_nos_delhi]
df_mumbai = df.loc[index_nos_mumbai]

# Remove the rows having no 'sub_region_2' in the dataframe of Delhi
df_delhi.drop(df_delhi[df_delhi['sub_region_2'].isnull() == True].index, inplace=True)

# On a particular date, take the average of transit and retail mobility for all sub-regions of Delhi and Mumbai
grouped_df_delhi = (df_delhi.groupby('date').sum())/11
grouped_df_mumbai = (df_mumbai.groupby('date').sum())/2

# Extract and store dates for plotting
dates = df_delhi['date'].drop_duplicates(keep='first')

# Make a list storing the ticks which are to be given on the x-axis
tick = [datetime(2021,1,1),datetime(2021,2,1),datetime(2021,3,1),datetime(2021,4,1),datetime(2021,5,1),datetime(2021,6,1),datetime(2021,7,1),datetime(2021,8,1),datetime(2021,9,1),datetime(2021,10,1),datetime(2021,11,1),datetime(2021,12,1),]
# Make a list storing the labels for each of these ticks
label = ['Jan\n2021','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Plot the retail mobility for Delhi and Mumbai on the same plane
plt.plot(dates,grouped_df_delhi['retail_and_recreation_percent_change_from_baseline'])
plt.plot(dates,grouped_df_mumbai['retail_and_recreation_percent_change_from_baseline'])

# Annotate the plot
# Give legend, ticks,labels and title to the plot
plt.legend(['Delhi','Mumbai'])
plt.xticks(ticks=tick,labels=label)
plt.xlabel('Time in Month')
plt.ylabel('Retail Mobility')
plt.title('Retail Mobility v/s Time')
# Display the grids and show the plot
plt.grid()
plt.show()

# Leave a blank line
print()


# Part B
# Annotate the output screen that part B begins here
print('Part B')

# Plot the transit mobility for Delhi and Mumbai on the same plane
plt.plot(dates,grouped_df_delhi['transit_stations_percent_change_from_baseline'])
plt.plot(dates,grouped_df_mumbai['transit_stations_percent_change_from_baseline'])

# Annotate the plot
# Give legend, ticks,labels and title to the plot
plt.legend(['Delhi','Mumbai'])
plt.xticks(ticks=tick,labels=label)
plt.xlabel('Time in Month')
plt.ylabel('Transit Mobility')
plt.title('Transit Mobility v/s Time')
# Display the grids and show the plot
plt.grid()
plt.show()

# Leave a blank line
print()


# Part D
# Annotate the output screen that part D begins here
print('Part D')

# Calculate the IQR of Retail and Transit mobilities for Delhi and Mumbai
# Print the value on the screen after rounding off the values to two decimal places
print('IQR of Retail mobility in Delhi is ' + str(round(grouped_df_delhi['retail_and_recreation_percent_change_from_baseline'].quantile(q=0.75)-grouped_df_delhi['retail_and_recreation_percent_change_from_baseline'].quantile(q=0.25),2)) + '.')
print('IQR of Transit mobility in Delhi is ' + str(round(grouped_df_delhi['transit_stations_percent_change_from_baseline'].quantile(q=0.75)-grouped_df_delhi['transit_stations_percent_change_from_baseline'].quantile(q=0.25),2))  + '.')
print('IQR of Retail mobility in Mumbai is ' + str(round(grouped_df_mumbai['retail_and_recreation_percent_change_from_baseline'].quantile(q=0.75)-grouped_df_mumbai['retail_and_recreation_percent_change_from_baseline'].quantile(q=0.25),2)) + '.')
print('IQR of Transit mobility in Mumbai is ' + str(round(grouped_df_mumbai['transit_stations_percent_change_from_baseline'].quantile(q=0.75)-grouped_df_mumbai['transit_stations_percent_change_from_baseline'].quantile(q=0.25),2)) + '.')

# Leave a blank line
print()


# Part E
# Annotate the output screen that part E begins here
print('Part E')

# Calculate the expected value of Retail and Transit mobilities for Delhi and Mumbai
# Print the value on the screen after rounding off the values to two decimal places
print('Expected value of Retail mobility in Delhi is ' + str(round(grouped_df_delhi['retail_and_recreation_percent_change_from_baseline'].mean(),2)) + '.')
print('Expected value of Transit mobility in Delhi is ' + str(round(grouped_df_delhi['transit_stations_percent_change_from_baseline'].mean(),2)) + '.')
print('Expected value of Retail mobility in Mumbai is ' + str(round(grouped_df_mumbai['retail_and_recreation_percent_change_from_baseline'].mean(),2)) + '.')
print('Expected value of Transit mobility in Mumbai is ' + str(round(grouped_df_mumbai['transit_stations_percent_change_from_baseline'].mean(),2)) + '.')
