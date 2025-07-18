import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Month':['Jan','Feb','Mar','Apr','May'],
    'Sales':[200,250,300,280,320],
    'Profit':[50,70,90,85,95]
    }

df=pd.DataFrame(data)

df.set_index('Month')['Sales'].plot(kind='pie',autopct='%1.1f%%',figsize=(6,6),startangle=90)
plt.title('Sales Distribution - Pie Chart')
plt.ylabel('') #Hide Y-axis label
plt.show()