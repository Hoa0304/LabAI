from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X = [[1200], [1500], [2000], [2500], [3000]]
y = [200000, 250000, 300000, 400000, 500000]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, predictions))

##================================================================
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([100, 150, 200, 250, 300])

model = LinearRegression().fit(X, y)
print("Dự đoán giá nhà:", model.predict([[6]]))
