import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.metrics import accuracy_score

#Calculate the eucledian distance between two points
def dist(x,y):
    return np.sqrt(np.sum((x - y) ** 2))

#Class to implement the functionality of KNN for classification
class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X_train, y_train):
        #Fit the training data.
        self.X_train = X_train
        self.y_train = y_train

    def _predict(self, x_pred):
        #Predict the class values for the predict data
        distance_list = [dist(x_pred,x_train) for x_train in X_train]
        min_k = np.argsort(distance_list)[:self.k]
        nearestk = [y_train[neigh] for neigh in min_k]
        common_values = Counter(nearestk).most_common()
        if len(common_values) == 0:
            return None
        return common_values[0][0]

    def predict(self, X_pred):
        predict_values = [self._predict(x) for x in X_pred]
        return predict_values
    
if __name__ == '__main__':
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
    clf = KNN(k=7)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("Actual    : " + str(y_test.tolist()))
    print("Predicted : " + str(predictions))
    accuracy = accuracy_score(y_pred=predictions,y_true=y_test)
    print("Accuracy : " + str(accuracy))