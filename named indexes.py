import pandas as pd

data ={
    'calories':[420,380,390],
    'duration':[50,40,45]
}

#load data into dataframe objects:
df=pd.DataFrame(data, index =['day1','day2','day3'])

print(df)

