import numpy as np
import matplotlib.pyplot as plt

# Параметры распределения
a, b = 0, 2  # границы распределения
C = 0.5      # нормировочная константа
mean = 2/3   # математическое ожидание
var = 2/9    # дисперсия
std = np.sqrt(var)  # среднее квадратическое отклонение

# Создаем фигуру
plt.figure(figsize=(12, 6))

# Генерируем точки для графика плотности
x = np.linspace(a-0.5, b+0.5, 500)
f = np.piecewise(x, [x < a, (x >= a) & (x <= b), x > b], 
                [0, lambda x: C*(2 - x), 0])

# Рисуем график плотности
plt.plot(x, f, 'b-', linewidth=2, label='Плотность вероятности $f(x)$')

# Отмечаем математическое ожидание
plt.axvline(mean, color='red', linestyle='--', linewidth=2, 
           label=f'Мат. ожидание $M[X] = {mean:.3f}$')

# Отмечаем дисперсию
plt.axvline(var, color='purple', linestyle='--', linewidth=2,
           label=f'Дисперсия $D[X] = {var:.3f}$')

# Отмечаем границы стандартного отклонения
plt.axvline(mean - std, color='green', linestyle=':', linewidth=2,
           label=f'Среднекв. отклонение $σ = {std:.3f}$')
plt.axvline(mean + std, color='green', linestyle=':', linewidth=2)

# Добавляем легенду и оформление
plt.title('Визуализация характеристик распределения', pad=20)
plt.xlabel('Значения случайной величины $X$')
plt.ylabel('Плотность вероятности $f(x)$')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.xlim(a-0.5, b+0.5)
plt.ylim(0, 1.1)

plt.tight_layout()
plt.show()