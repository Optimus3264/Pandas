import pandas as pd

df=pd.read_csv('exercise_data.csv')
x = df['Calories'].median()
df['Calories'].fillna(x,inplace=True)
print(df)