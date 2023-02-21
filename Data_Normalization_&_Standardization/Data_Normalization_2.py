#Data_normalization_2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocesing import MinMaxScaler

data_raw = np.array([
    [2, 3, 7, 30],
    [9, 4, 6, 1],
    [8, 15, 2, 40],
    [20, 10, 2, 6]
])

scaler = MinMaxScaler()
data_scale = scaler.fit_transform(data_raw)