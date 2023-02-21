import numpy as np
import pandas as pd

new_data = np.array([23, 56, 45, 65, 59, 55, 62, 54, 85, 25, 55])
print(pd.DataFrame(new_data).describe())