import numpy as np
import matplotlib.pyplot as plt

# Параметры распределения
C = 0.5
a, b = 0, 2

# Создаем данные
x = np.linspace(-0.5, 2.5, 500)
f = np.piecewise(x, [x < a, (x >= a) & (x <= b), x > b], 
                [0, lambda x: C*(2 - x), 0])
F = np.piecewise(x, [x < a, (x >= a) & (x <= b), x > b],
                [0, lambda x: x - x**2/4, 1])

# Создаем фигуру с двумя подграфиками
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# График 1: Через плотность вероятности
ax1.plot(x, f, 'b-', linewidth=2)
ax1.fill_between(x, f, where=(x>=1)&(x<=2), color='blue', alpha=0.3)
ax1.set_title('1. Через плотность вероятности')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.text(1.5, 0.1, 'P(X>1) = 0.25', ha='center')

# График 2: Через интегральную функцию
ax2.plot(x, F, 'r-', linewidth=2)
ax2.fill_between(x, F, where=(x>=1), color='red', alpha=0.1)
ax2.axvline(x=1, color='k', linestyle='--')
ax2.set_title('2. Через интегральную функцию')
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')
ax2.text(1.5, 0.5, 'P(X>1) = 1 - F(1) = 0.25', ha='center')

# Настройки общего отображения
plt.tight_layout()
plt.show()
