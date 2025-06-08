import pandas as pd
data = {
    'calories':[420,380,390],
    'duration':[50,40,45]    
}

#Load data into DataFrame object:
df=pd.DataFrame(data,index = ['Day 1','Day 2','Day 3'])

print(df)  #output is whole DataFrame
print(df.loc['Day 2']) #output is loc[index] in DataFrame