import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import mean_squared_error

class LinearRegression:
    def __init__(self, lr = 0.001, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.n_iters):
            y_pred = np.dot(X,self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T,(y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)

            #Weights are updated
            self.weights = self.weights - dw * self.lr
            self.bias = self.bias - db * self.lr
    
    def pred(self, X):
        y_pred = np.dot(X,self.weights) + self.bias
        return y_pred




X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
    
reg = LinearRegression(lr=0.5,n_iters=1000)
reg.fit(X_train,y_train)
predictions = reg.pred(X_test)

mse = mean_squared_error(y_pred=predictions, y_true=y_test)
print("Measn Sq Error: " + str(mse))


import matplotlib.pyplot as plt
y_pred_line = reg.pred(X)
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8,6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')
plt.show()