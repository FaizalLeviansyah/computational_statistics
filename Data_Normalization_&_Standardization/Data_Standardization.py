#Data_normalization_2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocesing import MinMaxScaler, StandardScaler

data_raw = np.array([
    [2, 3, 7, 30],
    [9, 4, 6, 1],
    [8, 15, 2, 40],
    [20, 10, 2, 6]
])

stand = StandardScaler()
data_stand = stand.fit_transform(data_raw)

plt.boxplot(data_stand)