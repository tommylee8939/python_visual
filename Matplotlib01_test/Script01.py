import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure()
x = np.linspace(1,10,100)
plt.plot(x,np.sin(x))


plt.figure()
x = np.linspace(1,10,100)
plt.plot(x,np.sin(x))


plt.show() # 위의 figure가 2개 있기 때문에 show()했을때 대화형 그래프 두개 생긴다