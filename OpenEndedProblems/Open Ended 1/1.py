import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-3, 7)
x = np.array([1, 4, 2, 3, 5, 2, 4, 1, 3, 2])

plt.figure(figsize=(8,4))
markerline, stemlines, baseline = plt.stem(n, x)

plt.title("1st Signal:")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.xticks(n)
plt.yticks([0,1,2,3,4,5])
plt.grid(True)
plt.show()
