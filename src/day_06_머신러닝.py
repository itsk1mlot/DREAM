# pip install scikit-learn
from sklearn import linear_model
import matplotlib.pyplot as plt
r = linear_model.LinearRegression()

height = [[121], [160], [166], [168], [170], [172], [173], [180]]
weight = [23, 54, 61, 65, 68, 70, 72, 79]
X = height
y = weight

r.fit(X, y)
coef = r.coef_
intercept = r.intercept_
print(f"weight = {coef} * height + ({intercept})")

score = r.score(X, y)
print("The score:", score)

############################################################################
#
#                                Show Data
#
############################################################################
new_data = [[150], [185]]
result = r.predict(new_data)

print("")
print(result)
for i in range(len(result)):
    print(f"📏 {new_data[i]}의 예상 몸무게: {result[i]}")

y_pred = r.predict(X)
print(y_pred)

plt.scatter(X, y, color='darkgreen')
plt.plot(X, y_pred, color='orange', linewidth=3)
plt.text(150, 40, "y = "+str(coef)+" * X + "+str(intercept))
plt.show()