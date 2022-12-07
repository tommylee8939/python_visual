import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure()
x = np.linspace(1,10,100)
plt.plot(x,np.sin(x))
plt.show()

plt.figure()
x = np.linspace(1,10,100)
plt.plot(x,np.cos(x))


plt.show()