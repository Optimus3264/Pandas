import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Month':['Jan','Feb','Mar','Apr','May'],
    'Sales':[200,250,300,280,320],
    'Profit':[50,70,90,85,95]
    }

df=pd.DataFrame(data)

df.plot(kind='scatter',x='Sales',y='Profit',color='green')
plt.title('Sales vs Profit - Scatter Plot')
plt.show()