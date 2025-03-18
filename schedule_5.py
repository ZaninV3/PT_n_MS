import matplotlib.pyplot as plt
import numpy as np

# Определение функции распределения F(x)
def F(x):
    if x < 30:
        return 0
    elif 30 <= x < 40:
        return 0.1
    elif 40 <= x < 50:
        return 0.3
    elif 50 <= x < 60:
        return 0.4
    elif 60 <= x < 70:
        return 0.6
    else:
        return 1

# Создание массива значений x
x_values = np.linspace(20, 80, 100)  # От 20 до 80 для охвата всех интервалов
y_values = [F(x) for x in x_values]  # Вычисление F(x) для каждого x

# Построение графика
plt.plot(x_values, y_values, color='green', label='F(x)')

# Подписи осей и заголовок
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.title('Функция распределения $F(x)$')

# Добавление сетки и легенды
plt.grid(True)
plt.legend()

# Отображение графика
plt.show()