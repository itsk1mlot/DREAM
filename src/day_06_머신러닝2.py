from sklearn import linear_model
import matplotlib.pyplot as plt
r = linear_model.LinearRegression()

# 키-성별
X = [[164, 1], [167, 1], [165, 0], [170, 0], [179, 0], [163, 1], [159, 0], [166, 1]]
y = [43, 48, 47, 66, 67, 50, 52, 44]

r.fit(X, y)
coef = r.coef_
intercept = r.intercept_

print("다차원 선형 회귀 방정식")
print(f"y = {coef} * X + ({intercept})")

print("적합도:", r.score(X, y))

############################################################################
#
#                                Show Data
#
############################################################################
new_data = [[166, 1], [166, 0]]
result = r.predict(new_data)
print(result)

for i in range(len(result)):
    print(f"{new_data[i]}의 예상 몸무게: {result[i]}")