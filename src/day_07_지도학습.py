import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

r = LinearRegression()
df_score = pd.read_csv('../data/score_updated.csv')
print(list(df_score))

X = df_score[["Hours"]]
y = df_score["Scores"]

print(df_score.corr())
sns.heatmap(df_score.corr(), annot=True, cmap="YlGnBu")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

r.fit(X_train, y_train)
coef = r.coef_
intercept = r.intercept_

print(f"성적 = {coef} * 공부시간 + {intercept}")

score = r.score(X, y)
print("The Score:", score)

y_pred = r.predict(X_test)
plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red')
plt.show()