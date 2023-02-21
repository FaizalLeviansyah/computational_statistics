# With Numpy
import numpy as np
apel = [100, 200, 150, 100, 120, 80, 90, 160, 110, 170]
avg_apel = no.mean(apel)
print(avg_apel)

#Median Example Using Numpy
import numpy as np
apel = [100, 200, 150, 100, 120, 80, 90, 160, 110, 170]
med_apel = np.median(apel)
apel.sort()
apel_urut = ' '.join(map(str, apel))
print('Apel sequence : {:s}'.format(apel_urut))
print(med_apel)

#Range - Example
import numpy as np

data = np.array([23, 56, 45, 65, 59, 55, 62, 54, 85, 25])
data_max = max(data)
data_min = min(data)
range = data_max - data_min
print(range)