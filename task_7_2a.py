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

# Построение полигона
plt.figure(figsize=(10, 5))
plt.plot(x, p_i, marker='o', linestyle='-', color='b', label='Полигон частот')
plt.title('Полигон относительных частот')
plt.xlabel('Середины интервалов')
plt.ylabel('Относительная частота ($p_i$)')
plt.grid(True)
plt.legend()
plt.show()