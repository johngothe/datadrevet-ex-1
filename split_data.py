import pandas as pd
df = pd.read_csv('smoking_driking_dataset_Ver01.csv')
MIN_AGE = 45
MAX_AGE = 55

def split_dataset(df, condition):
    """
    Split dataset into target (filtered) and source (remaining)
    based on a condition applied to a feature.
    """
    target_df = df.query(condition)
    source_df = df.loc[~df.index.isin(target_df.index)]
    print(f"Target size: {len(target_df)}, Source size: {len(source_df)}")
    return source_df, target_df

source_df, target_df = split_dataset(df, "(sex == 'Male') and (45 <= age <= 55)")

source_df.to_csv('source_data.csv', index=False)
target_df.to_csv('target_data.csv', index=False)

#df = df.drop(columns=['DRK_YN'])
filtered_df = df[(df['age'] >= MIN_AGE) & (df['age'] <= MAX_AGE)]
filtered_df.to_csv('filtered_data.csv', index=False)

# remaining data is source dataset for transfer learning
remaining_df = df[~df.index.isin(filtered_df.index)]
remaining_df.to_csv('remaining_data.csv', index=False)

print(f"Smaller dataset (filtered): {filtered_df.shape}")
print(f"Larger dataset (remaining): {remaining_df.shape}")
print(f"Full dataset (clean): {df.shape}")