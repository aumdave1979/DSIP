import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,12)
x = np.array([1, 3, 2, 4, 3, 5, 4, 2, 3, 1, 2, 0])

plt.figure(figsize=(6,4))
plt.step(n, x, where='post')
plt.xlim(0, 12)
plt.ylim(0, 3.5)

plt.title("2nd signal:")
plt.xlabel("n")
plt.ylabel("x[n]")

plt.xticks(np.arange(0,13,1))
plt.yticks(np.arange(0,4,1))
plt.grid(True)
plt.show()
