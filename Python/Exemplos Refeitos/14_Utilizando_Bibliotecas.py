from random import random
import matplotlib.pyplot as plt
valores = []
for i in range(10):
    valores.append(random())
print(valores)
plt.plot(valores)
plt.show()
