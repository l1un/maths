import matplotlib.pyplot as plt
import numpy as np

# averages, stds
x_mu, y_mu, x_sd, y_sd = 2, 3, 0.816, 2.160

# LaTeX denotation
x_bar, y_bar = r'$\bar{x}$', r'$\bar{y}$'
x_sd_label, y_sd_label = r'$s_{x}$', r'$s_{y}$'

# define coords
data = np.array([
    [1, 1],
    [2, 2],
    [2, 3],
    [3, 6],
])

# plot (T transpose) data, style plot points
x, y = data.T
plt.scatter(x, y, marker='x', s=60, color='black')
plt.annotate(
    s='', xy=(3.5, 6.5),
    xytext=(1, 0.5),
    arrowprops=dict(arrowstyle='<->', color='red'),
)
# style axis labels, title, scope
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('Correlation Coefficient Sample Data')
plt.ylim(0.5, 6.5)
plt.xlim(0.5, 3.5)

# add styles to display mean, std for x
#  plt.axvline(x.mean(), color='red', linestyle='dashed', linewidth=3)
#  plt.axvline(x.std(), color='red', linestyle='solid', linewidth=3)
#  plt.text(
    #  x.mean() + 0.15, 5,
    #  f'{x_bar} = {x.mean()}',
    #  bbox=dict(boxstyle='larrow', ec='black', facecolor='red', alpha=0.6),
    #  color='white'
#  )
#  plt.text(
    #  x.std() + 0.15, 5,
    #  f'{x_sd_label} = {round(x.std(ddof=1), 2)}',  # ddof: modify for sample
    #  bbox=dict(boxstyle='larrow', ec='black', facecolor='red', alpha=0.6),
    #  color='white'
#  )

# add styles to display mean, std for y
#  plt.axvline(y.mean(), color='green', linestyle='dashed', linewidth=3)
#  plt.axvline(y.std(), color='green', linestyle='solid', linewidth=3)
#  plt.text(
    #  y.mean() - 0.58, 2,
    #  f'{y_bar} = {y.mean()}',
    #  bbox=dict(boxstyle='rarrow', ec='black', facecolor='g', alpha=0.6),
    #  color='white'
#  )
#  plt.text(
    #  y.std() - 0.68, 2,
    #  f'{y_sd_label} = {round(y.std(ddof=1), 2)}',  # ddof: modify for sample
    #  bbox=dict(boxstyle='rarrow', ec='black', facecolor='g', alpha=0.6),
    #  color='white'
#  )

plt.show()
