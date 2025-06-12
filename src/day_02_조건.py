# try:
#     score = int(input("성적: "))
# except ValueError:
#     print("?")
#     exit()
#
# if (score > 100) or (score < 0):
#     print("?")
#     exit()
#
# if score >= 90:
#     print("합격입니다.")
#     print("장학금")
# else:
#     print("불합격입니다.")
#     print("화이팅")

"""number = int(input("숫자 입력: "))"""
# if number % 2 == 0:
#     print("짝")
# else:
#     print("홀")
#####################################
# if number > 0:
#     print("양수")
# elif number == 0:
#     print("0")
# else:
#     print("음수")
#####################################
# jari = len(str(number))
# # print(number, "는", jari, "자리 숫자")
# if number <= 100:
#     print(f"{number}는 3자리 숫자")
# elif number <= 10:
#     print(f"{number}는 2자리 숫자")
# else:
#     print(f"{number}는 1자리 숫자")
#
# print(f"{number}는 {jari}자리 숫자")
#####################################

# score = int(input("점수: "))
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

#####################################
from datetime import datetime

def is_leap(yr: int) -> bool:
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        return True
    else:
        return False

nowyear = datetime.now().year
print(f"올해는 {nowyear}년도")
if is_leap(nowyear):
    print(f"{nowyear}년은 윤년")
else:
    print(f"{nowyear}년은 윤년이 아님")

year = int(input("연도: "))
if is_leap(year):
    print(f"{year}년은 윤년")
else:
    print(f"{year}년은 윤년이 아님")

################################# 25.05.27.
# score = int(input("성적을 입력하시오: "))

# if score >= 90:
#     print("합격.")
#     print("장학금")
# else:
#     print("불합격")
#     print("파이팅")

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 7
#     print("C")
# else:
#     print("F")

# age = int(input("나이: "))
#
# if age >= 19:
#     print("성인")
# elif age >= 13:
#     print("청소년")
# elif age >= 0:
#     print("어린이")
# else:
#     print("잘못입력")