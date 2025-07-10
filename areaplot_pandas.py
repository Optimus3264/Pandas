import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Month':['Jan','Feb','Mar','Apr','May'],
    'Sales':[200,250,300,280,320],
    'Profit':[50,70,90,85,95]
    }

df=pd.DataFrame(data)

df.set_index('Month')[['Sales','Profit']].plot(kind='area',alpha=0.5)
plt.title('Sales and Profit - Area Plot')
plt.show()