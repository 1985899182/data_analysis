import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = np.array([1,2,35,12,3,4,7,5,4,5,1,6])
fig,ax = plt.subplots(1,1)
ax.hist(data)
ax.set_xticks(np.arange(0,35,3))

fig.show()