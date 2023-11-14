import pandas as pd

df_original = pd.read_csv('rankings.csv') 

artist_song_counts = df_original['artist'].value_counts()

df_original['appears_once'] = artist_song_counts[df_original['artist']].values == 1
df_original['appears_twice'] = artist_song_counts[df_original['artist']].values == 2

df_original['artist_group'] = df_original.apply(
    lambda row: '172 Artists' if row['appears_once'] else ('30 Artists' if row['appears_twice'] else row['artist']), 
    axis=1
)

final_csv_path = 'modified_rankings.csv'  
df_original.to_csv(final_csv_path, index=False)




