import pandas as pd


def get_data():
    # get data from wikipedia
    data = pd.read_html("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")

    # choose correct dataframe
    df = data[0]

    # Function to check if a value is an integer
    def is_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
     
    # Filter and convert       
    df['Year'] = df['Year'].apply(lambda x: int(x) if is_integer(x) else None)
    df.dropna(subset=['Year'], inplace=True)
    df['Year'] = df['Year'].astype(int)

    # find the most recent year
    max_year = df['Year'].max()

    winners = df[df.Year == max_year]['Physics'].iloc[0]

    return winners






