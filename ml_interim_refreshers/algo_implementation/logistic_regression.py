import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def sigmoid(x):
    return 1/(1 + np.exp(-x))

class LogisticRegression:
    def __init__(self, lr = 0.01, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_pred = np.dot(X, self.weights) + self.bias
            y_pred = sigmoid(linear_pred)
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            #Updating the weights
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db
    def pred(self, X):
        linear_pred = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_pred)
        bin_pred = [0 if y <= 0.5 else 1 for y in y_pred]
        return bin_pred

if __name__ == '__main__':
    bc = datasets.load_breast_cancer()
    X, y = bc.data, bc.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
        
    log_reg = LogisticRegression(lr=0.001,n_iters=1000)
    log_reg.fit(X_train,y_train)
    predictions = log_reg.pred(X_test)
    acc = accuracy_score(y_pred=predictions, y_true=y_test)
    print("Accuracy : " + str(acc))