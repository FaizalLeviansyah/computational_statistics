from scipy import stats
import statistics as s

value = [70, 80, 70, 70, 90, 100]

value_mode = stats.mode(value) #scipy
modus = s.mode(value) #Native Python
print(modus)
print(value_mode)
print(value_mode.mode)