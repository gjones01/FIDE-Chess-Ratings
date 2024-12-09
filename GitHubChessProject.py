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

top_fed = df['federation'].value_counts()
print('Top 5 Federations')
print(top_fed.head())

# Find the most common birth years
year = df['Birth Year'].value_counts()
print('Most Common Ages')
print(year.head(10))

# Find the youngest player
youngest = df['Birth Year'].min()
youngest_player = df[df['Birth Year'] == youngest]
print("Youngest Player(s):")
print(youngest_player[['name', 'Birth Year']])

#Let's Find the oldest player
oldest = df['Birth Year'].max()
oldest_player = df[df['Birth Year']== oldest]
print('Oldest Player(s):')
print(oldest_player[['name', 'Birth Year']])

#Elo Distribution
sns.histplot(df['ELO'], bins=20, kde=True)
plt.title('Distribution of ELO')
plt.show()

#Heatmap for ELO, games played and borth year
sns.heatmap(df[['ELO','Games','Birth Year']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()