import pandas as pd 


#Replace using Mean
df=pd.read_csv('exercise_data.csv')
x=df['Calories'].mean()
df['Calories'].fillna(x,inplace=True)

print(df)

