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



if __name__ == "__main__":
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
        
    reg = LinearRegression(lr=0.5,n_iters=1000)
    reg.fit(X_train,y_train)
    predictions = reg.pred(X_test)

    mse = mean_squared_error(y_pred=predictions, y_true=y_test)
    print("Measn Sq Error: " + str(mse))
