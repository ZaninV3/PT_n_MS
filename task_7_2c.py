import matplotlib.pyplot as plt

# Абсолютные частоты
n_i = [3, 5, 7, 12, 18, 16, 15, 10, 8, 6] 

# Границы интервалов
bins = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]

# Вычисляем накопленные частоты
N_i = []
cum_sum = 0
for count in n_i:
    cum_sum += count
    N_i.append(cum_sum)

# Точки для построения (правильные размеры)
x_points = bins  # [2, 5, 8, ..., 32] - 11 точек
y_points = [0] + [N/100 for N in N_i]  # [0, 0.03, 0.08, ..., 1] - 11 точек

# Построение графика
plt.figure(figsize=(10, 5))
plt.step(x_points, y_points, where='post', label='$F^*(x)$')
plt.title('Эмпирическая функция распределения')
plt.xlabel('Значения $x$')
plt.ylabel('$F^*(x)$')
plt.grid(True)
plt.legend()
plt.show()