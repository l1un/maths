import matplotlib.pyplot as plt
import numpy as np

rmse = 0.707

# define coords
actual_data = np.array([
    [1, 1],
    [2, 2],
    [2, 3],
    [3, 6],
])

predicted_data = np.array([
    [1, 0.5],
    [2, 3],
    [2, 3],
    [3, 5.5],
])

# plot (T transpose) data, style plot points
a, b = predicted_data.T
c, d = predicted_data.T - rmse
e, f = predicted_data.T + rmse

x, y = actual_data.T
plt.scatter(a, b, marker='.', color='red')

# fit line
fit = np.polyfit(x, y, 1)
fit_fn = np.poly1d(fit)
plt.plot(x, y, 'k.', x, fit_fn(x), '-r')

# regression lines
reg = np.polyfit(c, d, 1)
reg_fn = np.poly1d(reg)
plt.plot(c, d, 'k ', x, reg_fn(c), '--k', alpha=0.5)

reg2 = np.polyfit(e, f, 1)
reg_fn2 = np.poly1d(reg2)
plt.plot(e, f, 'k ', x, reg_fn2(e), '--k', alpha=0.5)


# style axis labels, title, scope
plt.xlabel('x')
plt.ylabel('y')
plt.title('Standard Deviation of Residuals')
plt.ylim(0, 6.5)
plt.xlim(0.5, 3.5)


plt.show()
