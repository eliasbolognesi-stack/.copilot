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

new_data = np.random.rand(100)
plt.scatter(new_data, new_data + np.random.rand(100) * 0.5, alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Dispersão')
plt.show()


