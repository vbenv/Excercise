import numpy as np
from scipy import stats

# 평균
mean = 23500

# 표준편차 계산
std = 3900

# 샘플 수
n = 100

# 표준오차 계산
se = std / np.sqrt(n)

# t 통계량 계산
z_stat = mean / se

# p-value 계산 (양측 검정)
p_value = 2 * (1 - stats.z.cdf(np.abs(z_stat)))

# 결과 출력
print(f"평균: {mean}")
print(f"표준편차: {std}")
print(f"표준오차: {se}")
print(f"z 통계량: {z_stat}")
print(f"p-value: {p_value}")

# 유의 수준
alpha = 0.05
print(f"1종 오류를 범할 최대 확률 (유의 수준): {alpha}")

# 유의 수준과 p-value 비교
if p_value < alpha:
    print("저장 기간이 소르빈산 잔류 농도에 영향을 미친다고 할 수 있는 충분한 증거가 있습니다.")
else:
    print("저장 기간이 소르빈산 잔류 농도에 영향을 미친다고 할 수 있는 충분한 증거가 없습니다.")
