# 비밀번호: 6자리 ~ 9자리 이하
N = int(input())# 첫 줄: N = 입력받을 문자열의 총 개수

for i in range (N):
    strings = input().strip()
    if 6 <= len(strings) <= 9:
        print("yes")
    else:
        print("no")#