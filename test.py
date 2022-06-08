import numpy as np
from scipy import linalg

import torch
import torch.nn as nn
import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt



import pandas as pd
data = pd.read_csv(r'./input/PeMSD7_V_228.csv')
data=data.values
print()

np.save('input/traffic_300.npy', data[:300])

# #
# # data = np.load('input/traffic_40.npy')
# plt.figure(figsize=(17, 6))
# x = range(400)
# for j in range(2):
#     y=[]
#     for i in range(400):
#         y.append(data[i][j])
#
#     plt.plot(x, y, 'o-', color='red', alpha=0.8, linewidth=1)
# plt.show()
#
#



