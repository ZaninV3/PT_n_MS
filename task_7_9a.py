from scipy.stats import t
import numpy as np

n = 100
mean = 17.29
s = 5.7932
gamma = 0.99

t_critical = t.ppf((1 + gamma)/2, df=n-1)
margin = t_critical * s / np.sqrt(n)

print(f"Доверительный интервал для μ: [{mean - margin:.2f}, {mean + margin:.2f}]")