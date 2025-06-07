import pandas as pd
data = {
    'calories':[420,380,390],
    'duration':[50,40,45]    
}

#Load data into DataFrame object:
df=pd.DataFrame(data)

print(df)  #output is whole DataFrame
print(df.loc[1]) #output is loc[index] in DataFrame