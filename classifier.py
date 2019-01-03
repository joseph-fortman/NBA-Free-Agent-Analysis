import numpy as np

#X = np.zeros((3,3))
X = np.genfromtxt('data/matrix.csv', delimiter=',')
X = np.delete(X, 0, 1)
print(X)

y = np.ones((3,1))
y[2] = 1
print(y)
[U,S,V] = np.linalg.svd(X, full_matrices=False)
print(U)
print(np.diag(S))
print(V)
# V is of the wrong dimensions right now
w_hat = V @ np.linalg.inv(np.diag(S)) @ U.T @ y
print(w_hat)
# dot product of X * X^T
#print(X @ X.T)
