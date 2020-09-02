import pandas as pd

df = pd.DataFrame({'col1': [2, 4, 1, 7, 8, 77], 'col2': [12, 34, 32, 76, 55, 66]})

df_zscore = df.copy()

cols = df.columns

for col in cols:
    df_col = df[col]

    z_score = (df_col - df_col.mean()) / df_col.std()

    df_zscore[col] = z_score.abs() > 0.5

print(df_zscore)