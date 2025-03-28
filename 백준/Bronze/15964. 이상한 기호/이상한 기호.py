A, B = map(int, input().split()) # 첫 째줄: A, B 입력
if (f"{A}@{B}"):
    result = (A+B)*(A-B)
print(result)