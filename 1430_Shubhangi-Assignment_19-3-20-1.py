print("\t\t\tAssignment\n\t\t\tShubhangi Goyal\n\t\t\tRoll No.: 17/1430\n\n")

# Importing dataset
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from sklearn.datasets import load_boston
boston_dataset = load_boston()

data = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
data.head()
data['MEDV'] = boston_dataset.target
print("\n\nData loaded\n\n")

# PREPROCESSING
# Considering useful columns and removing others
data = pd.DataFrame(np.c_[data['RM'],data['AGE'],data['MEDV']], columns = ['RM', 'AGE', 'MEDV'])

# Check null values
print("\n\nCheck null values\n",data.isnull().sum())
print("\nNo null values found\n")

# Discovering outliers by Z-Score
ZScore = np.abs(stats.zscore(data))
print("\n\nChecking where outliers are less than the ZScore")
print("ZScore > 1\n",np.where(ZScore > 1)[0],"\n",np.where(ZScore > 1)[1],"\n")
print("ZScore > 2\n",np.where(ZScore > 2)[0],"\n",np.where(ZScore > 2)[1],"\n")
print("ZScore > 3\n",np.where(ZScore > 3)[0],"\n",np.where(ZScore > 3)[1],"\n")

# Removing outliers
print("\n\nRemoving outliers (ZScore<3)\n")
data_o = data[(ZScore<3).all(axis=1)]
print ("Shape before removing outliers : ",np.shape(data),"\nShape after removing outliers : ",np.shape(data_o))

# Preparing the data for training
print("\n\nPreparing data for training\n")
X = pd.DataFrame(np.c_[data_o['RM'],data_o['AGE']], columns = ['RM', 'AGE'])
Y = pd.DataFrame(np.c_[data_o['MEDV']], columns = ['MEDV'])
print("\n\nX =\n",X.head(5))
print("\n\nY =\n",Y.head(5))

# Splitting dataset in Training sets and Test sets
print("\n\nSplitting dataset in Training sets and Test sets (with test_size=0.25)\n")
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25)
print("X_train.shape : ", X_train.shape, "\tX_test.shape", X_test.shape)
print("Y_train.shape : ", Y_train.shape, "\tY_train.shape", Y_train.shape)

# Linear Regression
print("\n\nLinear Regression")
lin_model = LinearRegression()
lin_model = lin_model.fit(X_train, Y_train)
predictions = lin_model.predict(X_test)

# Visualising predicted vs actual value
print("\n\nVisualising predicted vs actual value\n")
plt.scatter(Y_test, predictions)
plt.xlabel("True Values",color='red')
plt.ylabel("Predictions",color='blue')
plt.grid(True)
plt.show()

print("\n\nLinear Regression Score : ")
print(lin_model.score(X_test,Y_test)*100)

# Result of Linear Regression
mse = mean_squared_error(Y_test, predictions)
print("\n\nMean Square Error : ", mse)
