import pandas as pd

# get data from wikipedia
data = pd.read_html("https://en.wikipedia.org/wiki/Nathan's_Hot_Dog_Eating_Contest")

# choose correct dataframe
df = data[2]

# rename columns and choosing the right columns
df.rename(columns={'Winner (and date, if prior to permanently moving all contests to Independence Day in 1997)': 'winner'}, inplace=True)
df = df[['winner', 'Year']]

# clean data and add a gender column
df_clean = df[df['winner'].str.contains("MEN'S") | df['winner'].str.contains("WOMEN'S")][['winner', 'Year']]
df_clean['gender'] = df_clean['winner'].apply(lambda x: x.split(' ')[0])
df_clean['winner'] = df_clean['winner'].apply(lambda x: ' '.join(x.split(' ')[1:]))

# find the most recent year
max_year = df_clean['Year'].max()

# find the most recent winner for each gender
mens_winner = df_clean[(df_clean['Year'] == max_year) & (df_clean['gender'] == "MEN'S")]['winner'].values[0]
womens_winner = df_clean[(df_clean['Year'] == max_year) & (df_clean['gender'] == "WOMEN'S")]['winner'].values[0]

print(mens_winner, womens_winner)






