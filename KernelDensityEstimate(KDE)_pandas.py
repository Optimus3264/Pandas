import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Month':['Jan','Feb','Mar','Apr','May'],
    'Sales':[200,250,300,280,320],
    'Profit':[50,70,90,85,95]
    }

df=pd.DataFrame(data)

df['Sales'].plot(kind='kde',color='brown',linewidth=2)
plt.xlabel('Sales')
plt.title('Sales Density - KDE Plot')
plt.grid(True)
plt.show()