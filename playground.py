import numpy as np

a = np.array([1,2,3,4])
b = [7,8,9,10]
c = np.array(b)
print(np.stack((a, c)))