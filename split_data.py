import pandas as pd

MIN_AGE = 45
MAX_AGE = 55

df = pd.read_csv('smoking_driking_dataset_Ver01.csv')

#df = df.drop(columns=['DRK_YN'])
filtered_df = df[(df['age'] >= MIN_AGE) & (df['age'] <= MAX_AGE)]
filtered_df.to_csv('filtered_data.csv', index=False)

# remaining data is source dataset for transfer learning
remaining_df = df[~df.index.isin(filtered_df.index)]
remaining_df.to_csv('remaining_data.csv', index=False)

print(f"Smaller dataset (filtered): {filtered_df.shape}")
print(f"Larger dataset (remaining): {remaining_df.shape}")
print(f"Full dataset (clean): {df.shape}")