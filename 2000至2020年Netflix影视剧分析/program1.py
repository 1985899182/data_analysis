import numpy as np
import pandas as pd
df = pd.read_csv('netflix_titles.csv')
df_mv = df.loc[df['type'] == 'Movie']['release_year'].value_counts()
df_tv = df.loc[df['type'] == 'TV Show']['release_year'].value_counts()
df_concat = pd.concat([df_mv, df_tv], axis=0)
df_concat.sort_index(ascending=True)
for i in df_concat.iloc:
    print(i)