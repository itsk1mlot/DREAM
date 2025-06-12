# height = int(input("높이: "))
# if height <= 0:
#     print("높이는 1이상이여야 합니다")
#     exit()
# # height = 5
#
# """
# height = 5
#
#   i  | j | j-i     | hmmmmmm...
# i = 0: 1   (+1)    | i + 1 = j
# i = 1: 3   (+2)    | i + 2 = j
# i = 2: 5   (+3)    | i + 3 = j
# i = 3: 7   (+4)    | i + 4 = j
# i = 4: 9   (+5)    | i + 5 = j
#
#     *        (4)
#    ***       (3)
#   *****      (2)
#  *******     (1)
# *********    (0)
# """
#
# j = 1
# # print("--------------")
# for i in range(height):
#     val = i + j # (= 2 * i + 1)
#     star = '*' * val
#
#     # print("i: ", i)
#     # print("원하는거: ", i + j)
#     # print("star: ", star)
#     # print("--------------")
#
#     print(' ' * (height - i) + star)
#     j += 1
#
#######################################################################
#
# for i in range(1, 100):
#     if i % 3 == 0 or i % 7 == 0:
#         print(i, end=', ')
#
#######################################################################

# text = input("글자: ")
# r_data = ""
# for i in text:
#     r_data = i + r_data
# print(r_data)

#######################################################################

# for i in range(1, 7):
#     print(' ' * (6-i) + '*' * i) # ...

# for i in range(6, 0, -1):
#     print('*' * i)

# j = 0
# for i in range(1, 7):
#     j += 1
#     print('*' * i)

# num = input("")
# splited_num = num.split(" ")
# print(int(splited_num[0]) + int(splited_num[1]))

# cnt = 1
# sum = 0
#
# while cnt <= 100:
#     if cnt % 2 == 0:
#         sum += cnt
#     cnt += 1
#
# print("100아래짝수합:", sum)

numbers = [3, 2, -1, 5, -7, 6, -9, 10]
total = 0

print("양수: ", end='')

for num in numbers:
    if num < 0: continue

    total += num
    print(num, end=' ')

print("\n양수합:", total)