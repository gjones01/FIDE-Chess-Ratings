import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/gerryjr/Desktop/FIDERanking.csv')
#print(df) #This is testing to make sure the csv was correctly read in and printed

#Here I renamed the columns for some consistency in capitalization. It's more pleasing to the eye
df.rename(columns={'rank':'Rank','name' : 'Name','title': 'Title', 'federation' : 'Federation', 'games': 'Games','birth_year':'Birth Year'}, inplace = True)

#Let's see if there is any missing data
print(df.isnull().sum())

#Let's start looking at ELO stats
df.columns = df.columns.str.strip() #It seems we had some whitespace so we went a ahead anad stripped ot
print(df['ELO'].describe())

#Here we utilize .value_counts() and .head() to isolate the most populated federations
top_fed = df['federation'].value_counts()
print('Top 5 Federations')
print(top_fed.head())

# Here we utilize the .values_counts() and .head() again to isolate the most common birth years.
year = df['Birth Year'].value_counts()
print('Most Common Ages')
print(year.head(10))

# Now we want to see the name and birth year for the youngest chess player by setting a new variable as a minimum frame (youngest)
youngest = df['Birth Year'].min()
#Now we want to find any value in the 'Birth Year' column that is equal to the minimum value found in our 'youngest variable'
youngest_player = df[df['Birth Year'] == youngest]
#Now we simply print the name associated with the largest birth year (with a heading) and we see that it is Gukesh(2006).
print("Youngest Player(s):")
print(youngest_player[['name', 'Birth Year']])

#We want to find the oldest player(s) now by simply using .max() with a new varialbe titled 'oldest'. The same logic follows as to
#finding the youngest player(s) by birth year. In this case it is Miguel and Nigel (1965). 
oldest = df['Birth Year'].max()
oldest_player = df[df['Birth Year']== oldest]
print('Oldest Player(s):')
print(oldest_player[['name', 'Birth Year']])

#Now we want to see the distribution of ELO in terms of how many players have a particular ELO. Setting the bins in intervals of 20
#are sufficient for what we want to see.
sns.histplot(df['ELO'], bins=20, kde=True)
plt.title('Distribution of ELO')
plt.show()

#In this case we want o create a heatmap to study some correlations or lack thereof for ELO, the amount of games played and birth year
sns.heatmap(df[['ELO','Games','Birth Year']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

#This project aims to show basic skillsets and compentency with pandas, numpy, matlotlib and seaborn. I will do a follow up going
#a bit deeper into these FIDE statistic.
