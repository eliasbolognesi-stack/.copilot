import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 10) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)
plt.xlabel('Grupo')
plt.ylabel('Valor')
plt.title('Box Plot')
plt.show() 

data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.75, color='blue')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.show()

test = np.random.rand(10)
plt.plot(test, marker='o')  

