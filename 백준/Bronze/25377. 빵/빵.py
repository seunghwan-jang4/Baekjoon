N = int(input())# 가게의 수(테스트 케이스 개수)
result = []

for i in range(N):
    # A: 현재 위치에서 가게까지 걸리는 시간 , B: 빵 입고 시간
    A, B = map(int, input().split())
    if (A == B) or (A < B):
        result.append(B)

if len(result) == 0:
    print(-1)
else:
    print(min(result))