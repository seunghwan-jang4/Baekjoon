N = int(input())

# 기준 연도와 월
start_year = 2024
start_month = 8

interval = 7

# 총 경과 월 계산
elapsed_months = (N - 1) * interval

# 새로운 월과 추가 연도 계산
new_month = (start_month + elapsed_months) % 12
additional_years = (start_month + elapsed_months) // 12

# 월이 0일 경우 처리 (12월로 설정하고 연도 감소)
if new_month == 0:
    new_month = 12
    additional_years -= 1

# 최종 연도 계산
final_year = start_year + additional_years

# 결과 출력
print(final_year, new_month)