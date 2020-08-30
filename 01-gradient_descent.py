# FROM: https://gist.github.com/sagarmainkar/41d135a04d7d3bc4098f0664fe20cf3c

import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['ggplot'])

# 1. Creo una serie di dati di esempio e li visualizzo

# X = 2 + valore randomico
X = 2 * np.random.rand(100,1)
# Y = 4 + 3 * (X + valore randomico)
y = 4 + 3 * (X + np.random.randn(100,1))
# m = dimensione di X
m = X.size

# plt.plot(X, y, 'b.')
# plt.xlabel("$x$", fontsize=18)
# plt.ylabel("$y$", rotation=0, fontsize=18)
# _ = plt.axis([0,2,0,15])
# plt.show()

############################################################################

# 2. Cerco di identificare il valore migliore per O0 e O1.

X_b = np.c_[np.ones((100,1)), X]
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

############################################################################

# 3. Utilizzo i valori trovati al punto 2 per stimare y sulla base di un nuovo X

X_new = np.array([[0],[2]])
X_new_b = np.c_[np.ones((2,1)),X_new]
y_predict = X_new_b.dot(theta_best)

plt.plot(X_new,y_predict,'r-')
plt.plot(X,y,'b.')
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.axis([0,2,0,15])
plt.show()