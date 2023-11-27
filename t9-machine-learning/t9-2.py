import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

datos = r'C:\Users\pablo\PycharmProjects\test01\t9-machine-learning\Advertising.csv'

data = pd.read_csv(datos)

lm = smf.ols(formula='Sales~TV+Newspaper+Radio', data=data).fit()
print(lm.params)
print(lm.summary())

x = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

estimator = SVR(kernel='linear')
selector = RFE(estimator, n_features_to_select=2, step=1)
selector = selector.fit(x,y)

print(selector.support_)
