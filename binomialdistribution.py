from scipy.stats import binom
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1)
x = [1,2,3,4,5,6]
n, p = 6, 0.5
rv = binom(n,p)
ax.vlines(x,0,rv.pmf(x), colors = 'k', linestyles='-',lw=1,label='Probablity')

ax.legend(loc='best',frameon=False)
plt.show()
