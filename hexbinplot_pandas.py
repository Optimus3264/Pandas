import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Month':['Jan','Feb','Mar','Apr','May'],
    'Sales':[200,250,300,280,320],
    'Profit':[50,70,90,85,95]
    }



df2=pd.DataFrame({
    'X':np.random.randn(1000),
    'Y':np.random.randn(1000)+1
})
df2.plot(kind='hexbin',x='X',y='Y',gridsize=30,cmap='Blues')
plt.title('Hexbin Plot of Random Data')
plt.show()