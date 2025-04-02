import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 3, 500)  # График рисуется точечно
y = np.piecewise(x, 
                [(x >= 0) & (x <= 2), (x < 0) | (x > 2)],  # В остальных случаях график по нолям
                [lambda x: 0.5*(2 - x), 0])  # Тот самый отрезок С(2 - x)

plt.plot(x, y, 'b-', linewidth=2)  # Характеристика линии, сплошная, толщина 2
plt.title('График плотности вероятности f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()