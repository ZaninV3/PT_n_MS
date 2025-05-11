import matplotlib.pyplot as plt
import numpy as np

# Данные из вариационного ряда
intervals = [(2, 5), (5, 8), (8, 11), (11, 14), (14, 17), 
             (17, 20), (20, 23), (23, 26), (26, 29), (29, 32)]
n_i = [2, 6, 3, 10, 23, 18, 23, 8, 5, 2]
n = 100

# Середины интервалов
x = [(a + b) / 2 for a, b in intervals]

# Относительные частоты
p_i = [count / n for count in n_i]

# Границы интервалов
bins = [a for a, b in intervals] + [32]  # [2, 5, 8, ..., 32]

# Плотность частоты
density = [p / 3 for p in p_i]

# Построение гистограммы
plt.figure(figsize=(10, 5))
plt.bar(x, density, width=2.8, alpha=0.7, edgecolor='black', label='Гистограмма')
plt.title('Гистограмма относительных частот')
plt.xlabel('Интервалы')
plt.ylabel('Плотность частоты ($p_i / h$)')
plt.xticks(bins)
plt.grid(axis='y')
plt.legend()
plt.show()