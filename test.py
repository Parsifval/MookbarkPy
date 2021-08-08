import pprint
import pandas as pd

df = pd.read_csv('bookmarks.csv')
pprint.pprint(df)

user_input = input('What tag would you like to filter by')

newdf = df[(df.tags.str.contains(user_input))]
print(newdf)

