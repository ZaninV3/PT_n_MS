import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Данные из пункта 2
intervals = [(2, 5), (5, 8), (8, 11), (11, 14), (14, 17), 
             (17, 20), (20, 23), (23, 26), (26, 29), (29, 32)]

# Абсолютные частоты
n_i = [2, 6, 3, 10, 23, 18, 23, 8, 5, 2]

# Границы интервалов
bins = [a for a, b in intervals] + [32]  # [2, 5, 8, ..., 32]

# Вычисляем накопленные частоты
N_i = []
cum_sum = 0
for count in n_i:
    cum_sum += count
    N_i.append(cum_sum)

# Точки для построения (правильные размеры)
x_points = bins  # [2, 5, 8, ..., 32] - 11 точек
y_points = [0] + [N/100 for N in N_i]  # [0, 0.03, 0.08, ..., 1] - 11 точек



# Теоретическая плотность
x = np.linspace(2, 32, 100)



# Теоретическая функция
F_x = norm.cdf(x, loc=17.45, scale=5.71)

# Построение
plt.figure(figsize=(10, 5))
plt.step(x_points, y_points, where='post', label='$F^*(x)$')
plt.plot(x, F_x, 'r-', label='Теоретическая $F(x)$')
plt.title('Эмпирическая и теоретическая функции распределения')
plt.xlabel('Значения')
plt.ylabel('Вероятность')
plt.legend()
plt.grid()
plt.show()