import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3, 500)
F = np.piecewise(x,
                [x < 0, (x >= 0) & (x <= 2), x > 2],
                [0, lambda x: x - x**2/4, 1])

plt.plot(x, F, 'b-', linewidth=2)
plt.title('Интегральная функция распределения F(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axhline(1, color='black', linewidth=0.5, linestyle='--')
plt.show()