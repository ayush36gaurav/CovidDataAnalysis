# Import Pandas for working with dataframe
import pandas as pd
# Import matplotlib for plotting
import matplotlib.pyplot as plt


# Part A
# Annotate the output screen that part A begins here
print('Part A')

# Read the .csv with only specific columns
df = pd.read_csv('Cases.csv',usecols=['Date','District','Confirmed','Recovered','Deceased'])

# Change the data type of the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Make variables to store the populations of Delhi, Mumbai and Kolkata
population_delhi = 20591874
population_mumbai = 20667656
population_kolkata = 14850000

# Find indexes in the data drame which contain the data for Delhi, Mumbai and Kolkata
index_nos_delhi = df[df['District'] == 'Delhi'].index
index_nos_mumbai = df[df['District'] == 'Mumbai'].index
index_nos_kolkata = df[df['District'] == 'Kolkata'].index

# Make separate dataframe for each of Delhi, Mumbai and Chennnai using the indexes found above
df_delhi = df.loc[index_nos_delhi]
df_mumbai = df.loc[index_nos_mumbai]
df_kolkata = df.loc[index_nos_kolkata]

# Add new column for 'Infected Fraction' in each of the three dataframes and store values of it in it
# Use formula for 'Infected Fraction' given in the question
df_delhi['Infected Fraction'] = (df_delhi['Confirmed'] - df_delhi['Recovered'] - df_delhi['Deceased'])/(population_delhi)
df_mumbai['Infected Fraction'] = (df_mumbai['Confirmed'] - df_mumbai['Recovered'] - df_mumbai['Deceased'])/(population_mumbai)
df_kolkata['Infected Fraction'] = (df_kolkata['Confirmed'] - df_kolkata['Recovered'] - df_kolkata['Deceased'])/(population_delhi)

# Make new dataframes for each of Delhi, Mumbai and Kolkata containing data only for last day of month
df_delhi_monthwise = df_delhi.loc[df_delhi[df_delhi['Date'].dt.is_month_end == True].index]
df_mumbai_monthwise = df_mumbai.loc[df_mumbai[df_mumbai['Date'].dt.is_month_end == True].index]
df_kolkata_monthwise = df_kolkata.loc[df_kolkata[df_kolkata['Date'].dt.is_month_end == True].index]


# Store dates in a separate variable for plotting
dates = df_delhi_monthwise['Date']
# Make a list storing the ticks which are to be given on the x-axis
tick = df_delhi_monthwise['Date']
# Make a list storing the labels for each of these ticks
label = ['Apr','','','July','','','Oct','','','Jan\n2021','','','Apr','','','July','','','Oct']

# Use matplotlib and plot the 'Infected Fraction' for Delhi, Mumbai and Kolkata
plt.plot(dates,df_delhi_monthwise['Infected Fraction'])
plt.plot(dates,df_mumbai_monthwise['Infected Fraction'])
plt.plot(dates,df_kolkata_monthwise['Infected Fraction'])

# Annotate the plot
# Give legend, ticks,labels and title to the plot
plt.legend(['Delhi','Mumbai','Kolkata'])
plt.xticks(ticks=tick,labels=label)
plt.xlabel('Time in Month')
plt.ylabel('Infected Fraction')
plt.title('Infected Fraction v/s Time')
# Display the grids and show the plot
plt.grid()
plt.show()

# Leave a blank line
print()


# Part B
# Annotate the output screen that part B begins here
print('Part B')

# Calculate the variance of 'Infected Fraction' for each of Delhi, Mumbai and Kolkata
var_delhi = df_delhi['Infected Fraction'].var()
var_mumbai = df_mumbai['Infected Fraction'].var()
var_kolkata = df_kolkata['Infected Fraction'].var()

# Print the value on the screen
print('Variance of infected fraction in Delhi is ' + str(var_delhi) + '.')
print('Variance of infected fraction in Mumbai is ' + str(var_mumbai) + '.')
print('Variance of infected fraction in Kolkata is ' + str(var_kolkata) + '.')

# Leave a blank line
print()


# Extra work
# Annotate the output screen that Extra Work part begins here
print('Extra Work')

# Add new columns for 'Susceptible' and 'Removed' in the dataframe for Delhi and Mumbai and store values of 'Susceptible' in it
# Use formula for 'Susceptible' and 'Removed' given in the question
df_delhi_monthwise['Susceptible'] = (population_delhi - df_delhi_monthwise['Confirmed'])/(population_delhi)
df_mumbai_monthwise['Susceptible'] = (population_mumbai - df_mumbai_monthwise['Confirmed'])/(population_mumbai)
df_delhi_monthwise['Removed'] = (df_delhi_monthwise['Recovered'] + df_delhi_monthwise['Deceased'])/(population_delhi)
df_mumbai_monthwise['Removed'] = (df_mumbai_monthwise['Recovered'] + df_mumbai_monthwise['Deceased'])/(population_mumbai)

# Use  amtplotlib and plot 'Infected Fraction', 'Susceptible' and 'Removed' for Delhi on the same plot
plt.plot(dates,df_delhi_monthwise['Infected Fraction'])
plt.plot(dates,df_delhi_monthwise['Susceptible'])
plt.plot(dates,df_delhi_monthwise['Removed'])

# Display the legends, mark the ticks on x-axes and label the axes
plt.legend(['Infected Fraction','Susceptible','Removed'])
plt.xticks(ticks=tick,labels=label)
plt.xlabel('Time in Month')
plt.ylabel('log(Value)')
# Use logarithmic scale on y-axes
plt.yscale('log')

# Give title to the plot, display grids and show the plot
plt.title('Delhi\nValue v/s Time')
plt.grid()
plt.show()

# Use  amtplotlib and plot 'Infected Fraction', 'Susceptible' and 'Removed' for Mumbai on the same plot
plt.plot(dates,df_mumbai_monthwise['Infected Fraction'])
plt.plot(dates,df_mumbai_monthwise['Susceptible'])
plt.plot(dates,df_mumbai_monthwise['Removed'])

# Display the legends, mark the ticks on x-axes and label the axes
plt.legend(['Infected Fraction','Susceptible','Removed'])
plt.xticks(ticks=tick,labels=label)
plt.xlabel('Time in Month')
plt.ylabel('log(Value)')
# Use logarithmic scale on y-axes
plt.yscale('log')

# Give title to the plot, display grids and show the plot
plt.title('Mumbai\nValue v/s Time')
plt.grid()
plt.show()