import matplotlib.pyplot as plt
from scipy.stats import norm

intervals = [(2, 5), (5, 8), (8, 11), (11, 14), (14, 17), (17, 20), (20, 23), (23, 26), (26, 29), (29, 32)]
n_i = [2, 6, 3, 10, 23, 18, 23, 8, 5, 2]
n = 100
p_i = [count / n for count in n_i]  # относительные частоты
midpoints = [(a + b)/2 for a, b in intervals]  # середины интервалов

mu, sigma = 17.29, 5.7932
theoretical_p = [norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma) for a, b in intervals]


plt.figure(figsize=(12, 6))
plt.plot(midpoints, p_i, 'bo-', label='Эмпирические $p_i^*$')
plt.plot(midpoints, theoretical_p, 'ro--', label='Теоретические $p_i$')
plt.title('Сравнение относительных частот')
plt.xlabel('Середины интервалов')
plt.ylabel('Вероятность')
plt.legend()
plt.grid()
plt.show()