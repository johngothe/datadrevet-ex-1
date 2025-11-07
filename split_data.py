import pandas as pd

MIN_AGE = 40
MAX_AGE = 60

df = pd.read_csv('smoking_driking_dataset_Ver01.csv')

filtered_df = df[(df['age'] >= MIN_AGE) & (df['age'] <= MAX_AGE)]
filtered_df.to_csv('filtered_data.csv', index=False)
