from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
r = linear_model.LinearRegression()

score_df = pd.read_csv('../data/score.csv')
X = score_df[["Hours"]]
y = score_df["Scores"]

r.fit(X, y)
coef = r.coef_
intercept = r.intercept_

print("다차원 선형 회귀 방정식")
print(f"성적 = {coef} * 공부시간 + ({intercept})")

print("적합도:", r.score(X, y))

############################################################################
#
#                                Show Data
#
############################################################################
# new_data = [[166, 1], [166, 0]]
# result = r.predict(new_data)
# print(result)
#
# for i in range(len(result)):
#     print(f"{new_data[i]}의 예상 몸무게: {result[i]}")