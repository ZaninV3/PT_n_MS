import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры распределения
a, sigma = 12, 5
alpha, beta = 12, 22

# Данные для графика
x = np.linspace(a - 3*sigma, a + 3*sigma, 500)
y = norm.pdf(x, loc=a, scale=sigma)

# Создание графика
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b-', linewidth=2, label=f'$N({a}, {sigma}^2)$')

# Закрашиваем область P(12 < X < 22)
plt.fill_between(x, y, where=(x > alpha) & (x < beta), color='blue', alpha=0.3)


p = norm.cdf(beta, loc=a, scale=sigma) - norm.cdf(alpha, loc=a, scale=sigma)
print(f'P({alpha} < X < {beta}) = {p:.4f}')  # will print: P(12 < X < 22) = 0.4772



# Подписи и оформление
plt.title(f'Вероятность $P({alpha} < X < {beta}) = 0.4772$')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()