import random

max_streak_count = 0
streak_count = 0

li = ["가위", "바위", "보"]
win_dict = {
    "가위": "보", #가위는 보를 이김
    "바위": "가위", #바위는 가위를 이김
    "보": "바위", #보는 바위를 이김
}

def is_player_win(player_input, random_input):
    if player_input == random_input:
        return None

    print("랜덤 값:", win_dict.get(player_input))
    return True

while True:
    user_input = input("[가위/바위/보] 중 하나를 선택하세요 (엔터로 끝내기): ")
    if not user_input:
        print(f"게임 종료! (최고 연승 기록: {max_streak_count}회)")
        break

    if not user_input in li:
        print("only", li)
    rs = random.choice(li)
    is_win = is_player_win(user_input, rs)
    if is_win is None:
        print("비겼습니다!")
        if max_streak_count < streak_count:
            max_streak_count = streak_count
            print(f"최고 연승 기록 갱신! (최고 연승 기록: {max_streak_count}회)")
        streak_count = 0
    elif is_win:
        streak_count += 1
        print(f"이겼습니다! (현재 연승 기록: {streak_count}회 / 최고 연승 기록: {max_streak_count}회)")
    elif not is_win:
        print("졌습니다!")
        if max_streak_count < streak_count:
            max_streak_count = streak_count
            print(f"최고 연승 기록 갱신! (최고 연승 기록: {max_streak_count}회)")
        streak_count = 0
    else:
        print("오류 발생 :(")
        break

    print("")