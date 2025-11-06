import pandas as pd

df = pd.read_csv('SD.csv')

filtered_df = df[(df['age'] >= 40) & (df['age'] <= 60)]
filtered_df.to_csv('filtered_data.csv', index=False)
