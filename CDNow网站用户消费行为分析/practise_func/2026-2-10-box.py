import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = np.array([1,2,35,12,3,4,7,5,4,5,1,6]).reshape(3,4)
fig,ax = plt.subplots(1,1)
ax.boxplot(data.T,positions=[1,5,8])
ax.set_xticks(np.arange(0,10))
ax.set_xticklabels(np.arange(0,10))
fig.show()