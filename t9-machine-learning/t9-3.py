import pandas as pd
from sklearn.linear_model import LinearRegression

datos = r'C:\Users\pablo\PycharmProjects\test01\t9-machine-learning\Advertising.csv'
data = pd.read_csv(datos)

x_pred = data[['TV', 'Radio']]
y = data['Sales']

lm = LinearRegression()
lm.fit(x_pred, y)

print(lm.intercept_)
print(lm.coef_)
print(lm.score(x_pred, y))
