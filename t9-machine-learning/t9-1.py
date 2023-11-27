import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

datos = r'C:\Users\pablo\PycharmProjects\test01\t9-machine-learning\Advertising.csv'

data = pd.read_csv(datos)
print(data.head())
data.plot(kind='scatter', x='Radio', y='Sales')
data.plot(kind='scatter', x='Newspaper', y='Sales')
data.plot(kind='scatter', x='TV', y='Sales')

plt.show()
