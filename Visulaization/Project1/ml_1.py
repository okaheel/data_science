##

import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv("iris.csv", names=names)

print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size())

#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#pyplot.show()

#dataset.hist()
#pyplot.show()

#scatter_matrix(dataset)
#pyplot.show()

array = dataset.values
X = array[:,0:4]
y = array[:,4]

#using python to splice data into training and testing data

X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size = 0.20, random_state=1)
#print("split complete")

models = []
#logistic regression (LR)
models.append(("LR", LogisticRegression(solver = 'liblinear', multi_class='ovr')))
#Linear Discriminant Analysis (LDA)
models.append(("LDA", LinearDiscriminantAnalysis()))
#K-Nearest Neigbhors (KNN)
models.append(("KNN", KNeighborsClassifier()))
#Classification and regession Trees (CART)
models.append(('CART', DecisionTreeClassifier()))
#Gaussian Naive Bayes (NB)
models.append(('NB', GaussianNB()))
#support vector machines (SVM)
models.append(('SVM', SVC(gamma='auto')))

#evaluate each model

results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

#boxplot evaluating each algo
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()
