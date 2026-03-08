import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = np.array([1,2,35,12,3,4,7,5,4,5,1,6]).reshape(3,4)
print(data)
fig,ax = plt.subplots(1,1)
ax.violinplot(data.T,quantiles = [[],[],[0.9,0.4]])
fig.show()

