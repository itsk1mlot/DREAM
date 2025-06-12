# print(3.14, 56, "hello", True)
# print(type(3.14), type(56), type("hello"), type(True))
#
# s = "Hello World"
# print(s)
# print(s[0])
# print(len(s))
#
# print(str(3.14))
# print(type(str(3.14)))

x = int(input("첫번째 정수를 입력하시오: "))
y = int(input("두번째 정수를 입력하시오: "))
ind = input("기호: ")

rs = eval(str(x) + ind + str(y))
print(rs)

result = x + y
print(x, "와", y, "의 합은", result)