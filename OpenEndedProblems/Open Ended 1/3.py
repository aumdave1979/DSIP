import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-2,3)
x = []

for i in n:
    if i < 0:
        x.append(2)
    elif i <= 1:
        x.append(i + 2)
    else:
        x.append(1)

plt.figure(figsize=(6,4))
plt.plot(n,x)
plt.title("3rd signal:")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()