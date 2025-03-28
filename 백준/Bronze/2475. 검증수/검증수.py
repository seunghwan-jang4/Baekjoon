a, b, c, d, e = map(int, input().split()) # 첫째 줄: 고유번호 첫 5자리에 각각 빈칸을 하나씩 사이에 두고 입력.
unique_num = a, b, c, d, e
result = [(test_num**2) for test_num in unique_num] #
print(sum(result) % 10)