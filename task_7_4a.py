import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Данные из пункта 2
# Данные из вариационного ряда
intervals = [(2, 5), (5, 8), (8, 11), (11, 14), (14, 17), 
             (17, 20), (20, 23), (23, 26), (26, 29), (29, 32)]
n_i = [2, 6, 3, 10, 23, 18, 23, 8, 5, 2]
n = 100

# Относительные частоты
p_i = [count / n for count in n_i]

# Границы интервалов
bins = [a for a, b in intervals] + [32]  # [2, 5, 8, ..., 32]

# Плотность частоты
density = [p / 3 for p in p_i]



# Теоретическая плотность
x = np.linspace(2, 32, 100)
f_x = norm.pdf(x, loc=17.45, scale=5.71)

# Построение
plt.figure(figsize=(10, 5))
plt.bar(bins[:-1], density, width=3, alpha=0.5, label='Гистограмма')
plt.plot(x, f_x, 'r-', label='Теоретическая $f(x)$')
plt.title('Гистограмма и теоретическая плотность')
plt.xlabel('Значения')
plt.ylabel('Плотность')
plt.legend()
plt.grid()
plt.show()