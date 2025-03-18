# 입력 받기
N, X = map(int, input().split())  # 첫 줄에서 N과 X를 분리
A = list(map(int, input().split()))  # 두 번째 줄에서 수열 A를 리스트로 저장

# X보다 작은 수를 필터링하여 출력
result = [str(num) for num in A if num < X]  # 조건을 만족하는 숫자를 문자열로 변환하여 리스트에 저장
print(" ".join(result))  # 공백으로 구분하여 출력