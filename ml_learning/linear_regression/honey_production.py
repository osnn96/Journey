import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()

X = prod_per_year['year']
X = X.values.reshape(-1,1)

y = prod_per_year['totalprod']


plt.scatter(y,X)
plt.show()

regr = linear_model.LinearRegression()
regr.fit(X,y)
print(regr.coef_[0])
print(regr.intercept_)

y_predict = [pred for pred in regr.predict(X)]

plt.plot(y_predict, X)
plt.show()

X_future = np.array(range(2013,2051))
X_future = X_future.reshape(-1,1)

future_predict = [pred for pred in regr.predict(X_future)]

plt.plot(future_predict,X_future)
plt.show()

